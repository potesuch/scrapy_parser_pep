# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def open_spider(self, spider):
        self.pep_count = 0
        self.status_count = {}

    def process_item(self, item, spider):
        self.pep_count += 1
        self.status_count.setdefault(item['status'], 0)
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        result = []
        result.append(('Статус', 'Количество'))
        for k, v in self.status_count.items():
            result.append((k, v))
        result.append(('Total', self.pep_count))
        now = datetime.datetime.now()
        now_formatted = now.strftime('%Y-%m-%d_%H-%M-%S')
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(result)

