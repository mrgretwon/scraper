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

    # Uzywane sciezki xpath
    dane_lista = '//main[@class="content"]/article/section[@class="post-content"]'
    nast_strona = '//main[@class="content"]/ul/li[@class="pull-right"]/a/@href'
    item_fields = {
        'text': '//p/text()',
        'author': '//span[@class="author-content"]/h4/text()'
    }

    def parse(self, response):

        selector = HtmlXPathSelector(response)

        # iteracja przez dane_lista
        for dane in selector.select(self.dane_lista):
            loader = XPathItemLoader(TeoniteItem(), selector=dane)

            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # dodawanie xpath do loadera
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()

        for nastepna in selector.select(self.nast_strona):
            yield response.follow(nastepna, callback=self.parse)
