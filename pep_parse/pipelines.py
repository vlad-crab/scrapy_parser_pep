from collections import defaultdict
from pathlib import Path
import datetime as dt
import csv

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILE_NAME = f'status_summary_{dt.datetime.now().strftime(DATETIME_FORMAT)}.csv'
RESULTS_DIR_NAME = 'results'


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counter = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULTS_DIR_NAME
        results_dir.mkdir(exist_ok=True)
        file = results_dir / FILE_NAME
        self.status_counter['Total'] = sum(self.status_counter.values())
        with open(file, mode='w', encoding='utf-8', newline='') as csvfile:
            status_writer = csv.writer(csvfile)
            status_writer.writerow(['Статус', 'Количество'])
            status_writer.writerows(self.status_counter.items())
