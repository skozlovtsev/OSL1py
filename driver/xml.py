from .json import JSONDriver
import xmltodict

import xml

class XMLDriver(JSONDriver):
    @staticmethod
    def create(path: str, name: str) -> None:
        return JSONDriver.create(path, name)
    
    @staticmethod
    def write(path: str, data: list | dict) -> bool:
        ndata = {}
        ndata["root"] = data
        try:
            with open(path, 'w') as f:
                xmld = xmltodict.unparse(ndata)
                f.write(xmld)
            return True
        except FileExistsError:
            return False
    
    @staticmethod
    def read(path: str) -> list | dict:
        try:
            with open(path, 'r') as f:
                return xmltodict.parse(f.read())
        except FileExistsError:
            return None

    @staticmethod
    def delete(path: str, name: str) -> bool:
        return JSONDriver.delete(path, name)