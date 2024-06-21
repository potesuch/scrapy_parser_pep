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
    """
    Класс конвейера для обработки элементов PEP.

    Этот класс обрабатывает подсчет элементов PEP и их статусов.
    Он также создает CSV-отчет при завершении работы паука.
    """

    def open_spider(self, spider):
        """
        Инициализирует ресурсы при открытии паука.

        Args:
            spider (scrapy.Spider): Паук, который открывается.
        """
        self.pep_count = 0
        self.status_count = {}

    def process_item(self, item, spider):
        """
        Обрабатывает каждый элемент, проходящий через конвейер.

        Args:
            item (scrapy.Item): Обрабатываемый элемент.
            spider (scrapy.Spider): Паук, который собрал элемент.

        Returns:
            scrapy.Item: Обработанный элемент.
        """
        self.pep_count += 1
        self.status_count.setdefault(item['status'], 0)
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        """
        Завершает работу с ресурсами и создает итоговый отчет при закрытии паука.

        Args:
            spider (scrapy.Spider): Паук, который закрывается.
        """
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

