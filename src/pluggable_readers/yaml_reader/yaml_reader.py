import json

from libs.ProcessorInterface import ProcessorInterface
from utils.logger import logging
import yaml

logger = logging.getLogger(__name__)


class YamlFileReader(ProcessorInterface):
    def process(self, file_path: str):
        logger.info(f"Processing {file_path} file...")
        with open(file_path, 'r') as yaml_file:
            data = yaml.safe_load(yaml_file)
        print("-------------------- FILE CONTEXT ------------------------")
        print(data)
        print("-------------------- END of FILE CONTENT ------------------------")
