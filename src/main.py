from pathlib import Path
from pprint import pprint

from libs.file_processor import FileProcessor, get_processor_engine
from utils.logger import logging
import multiprocessing
import time


logger = logging.getLogger(__name__)


def process_file(file_path):
    all_engines = get_processor_engine()
    file_extension = file_path.suffix[1:]  # Get file extension without the dot
    possible_reader = f"{file_extension}_reader"
    processor_engine_names = list(all_engines.keys())
    if possible_reader in processor_engine_names:
        processor_engine_name = possible_reader
    else:
        return f"Invalid File: {file_path}"

    if processor_engine_name not in all_engines:
        return f"Processor engine '{processor_engine_name}' is not supported for file: {file_path}"

    selected_engine = all_engines[processor_engine_name]
    engine_obj = selected_engine["reader"].create_engine()
    processor = FileProcessor(engine_obj, file_path)
    processor.read()

def start():
    
    directory_path = "files"
    if not Path(directory_path).exists():
        logger.error("File not found in files/ directory.")

    directory = Path(directory_path)
    file_paths = [file for file in directory.iterdir() if file.is_file()]

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())  # Use all available CPU cores

    results = pool.starmap(process_file, [(file_path, ) for file_path in file_paths])

    for result in results:
        if result is not None:
            print(result)


def main() -> None:
    logging.info("Starting main...")
    try:
        start()

    except KeyboardInterrupt:
        logger.warning("Keyboard Interrupt by the User!!")


if __name__ == '__main__':
    main()
