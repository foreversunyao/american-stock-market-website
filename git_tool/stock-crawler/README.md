# Stock-crawler #

Stock Exchange crawler from Yahoo! Finance.

Overview
--------

This is an experiment using [Scrapy](http://scrapy.org/), a fast high-level screen scraping and web crawling framework made in Python.

#### Install ####

Install the requirements: 

```
pip install -r devops/requirements.txt
```

#### The Spider ####

Open the `crawler/spiders/stock_spider.py` file to see the logic and the URLs to be crawled.

#### Run ####

Inside the `/app` folder, run this command line to start crawling: 

```
scrapy crawl stock -o output/stock.json -t json
```
Open the generated file at `output/stock.json` and you'll get:

```json
[
    {
        "value": ["875,04"],
        "title": ["Google Inc. (GOOG)"]
    },
    {
        "value": ["23,63"],
        "title": ["Facebook, Inc. (FB)"]
    },
    {
        "value": ["430,05"],
        "title": ["Apple Inc. (AAPL)"]
    }
]
```
