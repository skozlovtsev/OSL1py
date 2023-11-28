from abc import ABC, abstractmethod


class Driver(ABC):
    @staticmethod
    @abstractmethod
    def create(path: str, name: str) -> bool:
        ...
     
    @staticmethod
    @abstractmethod
    def write(path: str, data: str | list | dict) -> bool:
        ...
    
    @staticmethod
    @abstractmethod
    def read(path: str) -> str | list | dict:
        ...

    @staticmethod
    @abstractmethod
    def delete(path: str, name: str) -> bool:
        ...
