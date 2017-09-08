from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from scraper_blog.items import TeoniteItem


class BlogSpider(BaseSpider):
    name = "blog"
    start_urls = [
        "https://teonite.com/blog/kickstarter-we-are-a-backer/",
    ]

    # searching data with xpath
    data_list = '//main[@class="content"]/article/section[@class="post-content"]'
    next_page = '//main[@class="content"]/ul/li[@class="pull-right"]/a/@href'
    item_fields = {
        'text': '//p/text()',
        'author': '//span[@class="author-content"]/h4/text()'
    }

    def parse(self, response):

        selector = HtmlXPathSelector(response)

        # iterate over data_list
        for data in selector.select(self.data_list):
            loader = XPathItemLoader(TeoniteItem(), selector=data)

            loader.default_input_processor = MapCompose(str.strip)
            loader.default_output_processor = Join()

            # add xpath to loader
            for field, xpath in self.item_fields.items():
                loader.add_xpath(field, xpath)
            yield loader.load_item()

        for nextp in selector.select(self.next_page):
            yield response.follow(nextp, callback=self.parse)
