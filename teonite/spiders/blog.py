import scrapy

class blogSpider(scrapy.Spider):
    name = "blog"
    allowed_domains = ["https://teonite.com"]
    start_urls = [
        "https://teonite.com/blog/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)