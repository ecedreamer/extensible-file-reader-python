from libs.ProcessorInterface import ProcessorInterface
from utils.logger import logging

logger = logging.getLogger(__name__)


__version__ = "2.4.0"

class TXTFileReader(ProcessorInterface):
    def process(self, file_path: str):
        logger.info(f"Processing {file_path} file...")
        with open(file_path, 'r') as file:
            content = file.read()
        logger.info("-------------------- FILE CONTEXT ------------------------")
        for line in content.split('\n'):
            print(line)
        logger.info("-------------------- END of FILE CONTENT ------------------------")
