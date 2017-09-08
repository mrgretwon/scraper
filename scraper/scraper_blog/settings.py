BOT_NAME = 'teonite'

SPIDER_MODULES = ['scraper_blog.spiders']
NEWSPIDER_MODULE = 'scraper_blog.spiders'


ROBOTSTXT_OBEY = True


DATABASE = {
    'drivername': 'postgres',
    'host': 'db',
    'port': '5432',
    'username': 'postgres',
    'password': 'bla1bla2',
    'database': 'scrape'
}

ITEM_PIPELINES = {
    'scraper_blog.pipelines.TeonitePipeline': 800,
}
