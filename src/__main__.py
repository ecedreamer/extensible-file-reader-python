from pathlib import Path
from pprint import pprint

from libs.file_processor import FileProcessor, get_processor_engine
from utils.logger import logging

logger = logging.getLogger(__name__)


def start() -> None:
    all_engines = get_processor_engine()
    print("Available Engines\n", {f"{name}_{engine['version']}" for name, engine in all_engines.items()})
    while True:
        file_name = input("Enter file name: ")
        file_path = f"files/{file_name}"
        if not Path(file_path).exists():
            logger.error("File not found in files/ directory.")
            continue

        processor_engine_name = input("Processor engine: ")
        if not all_engines.get(processor_engine_name):
            logger.error(f"Processor engine: {processor_engine_name} is not supported")
            continue

        selected_engine = all_engines.get(processor_engine_name)
        engine_obj = selected_engine.get("reader").create_engine()
        processor = FileProcessor(engine_obj, file_path)
        processor.process()


def main() -> None:
    logging.info("Starting main...")
    try:
        start()
    except KeyboardInterrupt:
        logger.warning("Keyboard Interrupt by the User!!")


if __name__ == '__main__':
    main()
