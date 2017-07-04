# Natural Language Processing (NLP) for Odia language.
NLP experiments for Odia language.

## Authors
* **Swarupananda Bissoyi** - (https://github.com/sbissoyi/nlp-odia)

## Building a corpus of Odia
Scrapy is used to scrape Odia unicode texts from popular newspaper websites.
###### Setting up scrapy (Windows)
```
- Install pip by running get-pip.py (https://bootstrap.pypa.io/get-pip.py)
- Install Visual Studio Community Edition 2015 or higher (due to dependencies)
- pip install lxml==3.6.0
- pip install pypiwin32
- pip install scrapy
```

###### Running scrapy
```
scrapy crawl mySpider -s download_maxsize=0 -o my-output.json
```
