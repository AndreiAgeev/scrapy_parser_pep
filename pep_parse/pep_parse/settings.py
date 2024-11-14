from .constants import FEED_URI

BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True

FEEDS = {
    FEED_URI: {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
        'encoding': 'utf8'
    }
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
