import json

from libs.ProcessorInterface import ProcessorInterface
from utils.logger import logging

logger = logging.getLogger(__name__)


class JSONFileReader(ProcessorInterface):
    def process(self, file_path: str):
        logger.info(f"Processing {file_path} file...")
        with open(file_path, 'r') as file:
            content = json.load(file)
        print("-------------------- FILE CONTEXT ------------------------")
        for item in content:
            print(item)
        print("-------------------- END of FILE CONTENT ------------------------")
