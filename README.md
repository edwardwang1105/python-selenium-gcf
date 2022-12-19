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
# prepare
pip install functions-framework
pip install -r requirements.txt

# run Functions Framework server with function target
functions-framework --target=haitou_scraping

# In a different terminal, curl the Functions Framework server
curl -X POST localhost:8080 \
   -H "Content-Type: application/cloudevents+json" \
   -d '{
	"specversion" : "1.0",
	"type" : "example.com.cloud.event",
	"source" : "https://example.com/cloudevents/pull",
	"subject" : "123",
	"id" : "A234-1234-1234",
	"time" : "2018-04-05T17:31:00Z",
	"data" : "hello world"
}'
```

# Deploy GCP Functions
```bash
# install serverless-chrome v1.0.0-37, chromedriver 2.37
sh installer.sh

# deploy GCP functions (gen2)
gcloud functions deploy scraping-function \
    --gen2 \
    --region asia-northeast1 \
    --runtime python39 \
    --entry-point haitou_scraping \
    --source . \
    --trigger-topic=haitou-scraping \
    --timeout=540 \
    --memory=1024
```

# References
- serverless-chrome: https://github.com/adieuadieu/serverless-chrome
- chromedriver: https://chromedriver.chromium.org/downloads