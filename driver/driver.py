from abc import ABC, abstractmethod


class Driver(ABC):
    @staticmethod
    @abstractmethod
    def create(path: str, name: str) -> None:
        ...
     
    @staticmethod
    @abstractmethod
    def write(path: str, data: str) -> bool:
        ...
    
    @staticmethod
    @abstractmethod
    def read(path: str) -> str:
        ...

    @staticmethod
    @abstractmethod
    def delete(path: str, name: str) -> bool:
        ...
