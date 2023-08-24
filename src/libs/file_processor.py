from typing import Dict, Type

from core_readers.txt_reader import TXTFileReader, __version__
from libs.ProcessorInterface import ProcessorInterface
from libs.ProcessorManager import PluginManager
from utils.logger import logging

logger = logging.getLogger(__name__)


class FileProcessor:
    def __init__(self, engine: ProcessorInterface, file_path: str) -> None:
        self.engine = engine
        self.file_path = file_path

    def read(self):
        self.engine.process(self.file_path)


def _get_core_engines() -> dict[str, dict[str, int | ProcessorInterface]]:
    return {
        "txt_reader": {
            "reader": TXTFileReader,
            "version": __version__
        }
    }


def get_processor_engine() -> dict[str, dict[str, int | ProcessorInterface]]:
    all_engines = _get_core_engines()
    manager = PluginManager()
    plugin_engines = manager.load_plugins()
   
    all_engines |= plugin_engines
    return all_engines
