# python-selenium-gcf-template
Run Python selenium with chromedriver on GCP Functions.

[![MIT license](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

# Versions
- Python library
    - python 3.9.9 (stable latest)
    - pip 21.3.1 (stable latest)
    - selenium 3.13.0 (fixed version depend on serverless-chrome version)
- Builded binary
    - serverless-chrome v1.0.0-37 for linux64 (fixed version depend on python 3.9)
    - chromedriver 2.37 for linux64 (fixed version depend on serverless-chrome)

# Run on Local
```bash
# create pipenv
# install functions-framework
pip install functions-framework

# run function
functions-framework --target=scraper
```

# Deploy GCP Functions
```bash
# install serverless-chrome v1.0.0-37, chromedriver 2.37
sh installer.sh

# deploy GCP functions
gcloud functions deploy scraper \
    --region asia-northeast1 \
    --runtime python39 \
    --allow-unauthenticated \
    --trigger-http \
    --memory=512
```

# References
- serverless-chrome: https://github.com/adieuadieu/serverless-chrome
- chromedriver: https://chromedriver.chromium.org/downloads