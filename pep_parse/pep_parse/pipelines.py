# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from collections import defaultdict
from datetime import datetime

from itemadapter import ItemAdapter

from .constants import DATETIME_FORMAT, RESULT_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_dict = defaultdict(int)
        self.status_dict['Статус'] = 'Количество'
        self.total = 0

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.status_dict[adapter['status']] += 1
        self.old_total = self.total
        self.total += 1
        return item

    def close_spider(self, spider):
        self.status_dict['Total'] = self.total
        RESULT_DIR.mkdir(exist_ok=True)
        now = datetime.now().strftime(DATETIME_FORMAT)
        filename = f'status_summary_{now}.csv'
        filepath = RESULT_DIR / filename
        with open(filepath, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, dialect='unix', quoting=csv.QUOTE_NONE)
            writer.writerows(self.status_dict.items())
