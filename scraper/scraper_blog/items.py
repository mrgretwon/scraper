from scrapy.item import Item, Field


class TeoniteItem(Item):
    text = Field()
    author = Field()
