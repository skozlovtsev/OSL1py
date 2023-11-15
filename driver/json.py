from .file import FileDriver

import json


class JSONDriver(FileDriver):
    @staticmethod
    def create(path: str, name: str) -> None:
        return super().create(path, name)
    
    @staticmethod
    def write(path: str, data: list | dict) -> bool:
        try:
            with open(path, 'w') as f:
                json.dump(data, f)
            return True
        except FileExistsError:
            return False
    
    @staticmethod
    def read(path: str) -> list | dict:
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileExistsError:
            return None
    
    @staticmethod
    def delete(path: str, name: str) -> bool:
        return super().delete(path, name)