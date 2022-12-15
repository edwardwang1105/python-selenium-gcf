import os
import time

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from selenium import webdriver


def scraper(request):
    # init google spreadsheet
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("配当").sheet1

    # init webdriver
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

    # start scraping
    code = sheet.cell(2, 1).value
    print(code)
    driver.get(f'https://kabutan.jp/stock/?code={code}')
    time.sleep(1)
    line = driver.find_element_by_class_name('si_i1_1').text
    print(line)
    sheet.update_cell(2, 2, line)
    driver.quit()
    return line
