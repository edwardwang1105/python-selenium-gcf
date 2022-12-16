import os
import time
from datetime import datetime, timedelta, timezone

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from selenium import webdriver


def scraper(data, context):
    # 初始化Google Spreadsheet
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("配当").sheet1

    # 初始化抓取工具
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"
    driver = webdriver.Chrome(
        os.getcwd() + "/bin/chromedriver", chrome_options=chrome_options)

    # 从Spreadsheet读取股票代码列表
    stock_code_list = sheet.col_values(2)[1:]  # B2以下的内容
    print(stock_code_list)

    # 对每个股票代码进行抓取
    for row_index, stock_code in enumerate(stock_code_list):
        # 指定要抓取的网页网址
        driver.get(f'https://kabutan.jp/stock/?code={stock_code}')
        time.sleep(1)

        # 抓取股价
        kabuka = driver.find_element_by_xpath('//*[@id="stockinfo_i1"]/div[2]/span[2]').text

        # 抓取趋势
        trends = []
        trend_elements = driver.find_elements_by_xpath('//*[@id="kobetsu_right"]/div[1]/table/tbody/tr[1]/td/img')
        for element in trend_elements:
            trends.append(element.get_attribute('alt'))

        # 写入Spreadsheet
        JST = timezone(timedelta(hours=+9), 'JST')
        write_data = [kabuka.replace('円', '')] + trends + [datetime.now(JST).strftime('%Y-%m-%d %H:%M:%S')]
        print(stock_code, write_data)
        for j in range(0, len(write_data)):
            sheet.update_cell(row_index + 2, j + 4, write_data[j])

    return 'Success'
