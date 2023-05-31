import csv

from libs.ProcessorInterface import ProcessorInterface
from utils.logger import logging

logger = logging.getLogger(__name__)


class CSVFileReader(ProcessorInterface):
    def process(self, file_path: str):
        logger.info(f"Processing {file_path} file...")
        with open(file_path, 'r') as file:
            content = csv.DictReader(file)
            content = list(content)
        print("-------------------- FILE CONTENT ------------------------")
        for item in content:
            print(item)
        print("-------------------- END of FILE CONTENT ------------------------")
