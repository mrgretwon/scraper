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
    dane_list_xpath = '//main[@class="content"]/article/section[@class="post-content"]'
    item_fields = {
        'text': '//p/text()',
        'author': '//span[@class="author-content"]/h4/text()'
    }

    def parse(self, response):

        selector = HtmlXPathSelector(response)

        # iterate over deals
        for dane in selector.select(self.dane_list_xpath):
            loader = XPathItemLoader(TeoniteItem(), selector=dane)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()

        for nastepna in response.xpath('//main[@class="content"]/ul/li[@class="pull-right"]/a/@href').extract():
            yield response.follow(nastepna, callback=self.parse)
