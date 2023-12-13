from os.path import exists
from os import remove
from .driver import Driver


class FileDriver(Driver):
    @staticmethod
    def create(path: str, name: str) -> bool:
        if exists(path + name):
            return False
        with open(path + name, 'a'):
            return True
     
    @staticmethod
    def write(path: str, data: str) -> bool:
        try:
            with open(path, 'a') as f:
                f.write(data)
                return True
        except FileNotFoundError:
            return False
    
    @staticmethod
    def read(path: str) -> str:
        try:
            with open(path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return None

    @staticmethod
    def delete(path: str, name: str) -> bool:
        try:
            remove(path + name)
            return True
        except FileNotFoundError:
            return False