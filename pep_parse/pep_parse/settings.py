from .constants import results_dir_name

BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True

FEEDS = {
   f'{results_dir_name}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
        'encoding': 'utf8'
    }
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
