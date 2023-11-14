from os.path import exists
from os import remove
from .driver import Driver


class FileDriver(Driver):
    @staticmethod
    def create(path: str, name: str, i:int = 0) -> None:
        if not exists(path + name):
            with open(path + name, 'a'):
                return
        i += 1
        FileDriver.create(path, name + f"({i})")
        return
     
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