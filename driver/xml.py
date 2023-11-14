from .file import FileDriver

import xml

class XMLDriver(FileDriver):
    @staticmethod
    def create(path: str, name: str, i: int = 0) -> None:
        return super().create(path, name, i)
    
    @staticmethod
    def write(path: str, data: str) -> bool:
        return super().write(path, data)
    
    @staticmethod
    def read(path: str) -> str:
        return super().read(path)
    
    @staticmethod
    def delete(path: str, name: str) -> bool:
        return super().delete(path, name)