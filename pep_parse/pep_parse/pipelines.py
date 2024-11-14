import csv
from collections import defaultdict
from datetime import datetime

from itemadapter import ItemAdapter

from .constants import DATETIME_FORMAT, RESULT_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_dict = defaultdict(int)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.status_dict[adapter['status']] += 1
        return item

    def close_spider(self, spider):
        self.status_dict['Total'] = sum(self.status_dict.values())
        now = datetime.now().strftime(DATETIME_FORMAT)
        filename = f'status_summary_{now}.csv'
        filepath = RESULT_DIR / filename
        print(filepath)
        with open(filepath, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, dialect='unix', quoting=csv.QUOTE_NONE)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.status_dict.items())
