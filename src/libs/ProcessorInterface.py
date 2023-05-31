from abc import ABC, abstractmethod


class ProcessorInterface(ABC):
    @classmethod
    def create_engine(cls):
        return cls()

    @abstractmethod
    def process(self, file_path: str):
        ...
