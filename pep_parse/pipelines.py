from collections import defaultdict
from pathlib import Path
import datetime as dt

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
        with open(file, mode='w', encoding='utf-8') as f:
            f.write('Статус, Количество\n')
            total = 0
            for status, count in self.status_counter.items():
                f.write(f'{status}, {count}\n')
                total += count
            f.write(f'Total,{total}\n')
