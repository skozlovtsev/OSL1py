from .json import JSONDriver
import xmltodict

import xml

class XMLDriver(JSONDriver):
    @staticmethod
    def create(path: str, name: str, i: int = 0) -> None:
        return super().create(path, name, i)
    
    @staticmethod
    def write(path: str, data: list | dict) -> bool:
        try:
            with open(path, 'w') as f:
                xmltodict.dump(data, f)
            return True
        except FileExistsError:
            return False
    
    @staticmethod
    def read(path: str) -> list | dict:
        try:
            with open(path, 'r') as f:
                return xmltodict.load(f)
        except FileExistsError:
            return None

    @staticmethod
    def delete(path: str, name: str) -> bool:
        return super().delete(path, name)