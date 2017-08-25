FROM python:3.6

MAINTAINER Lucek

LABEL version="1.0"

WORKDIR /code/

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD . .

ENTRYPOINT scrapy crawl blog_spider -o blog_spider.json
