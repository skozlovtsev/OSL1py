from abc import ABC, abstractmethod


class Driver(ABC):
    @abstractmethod
    @staticmethod
    def create(path: str, name: str) -> None:
        ...
     
    @abstractmethod
    @staticmethod
    def write(path: str, data: str) -> bool:
        ...
    
    @abstractmethod
    @staticmethod
    def read(path: str) -> str:
        ...

    @abstractmethod
    @staticmethod
    def delete(path: str, name: str) -> bool:
        ...
