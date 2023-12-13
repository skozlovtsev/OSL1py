import zipfile as zip
from .file import FileDriver


class ZipDriver(FileDriver):
    @staticmethod
    def create(path: str, name: str) -> bool:
        return FileDriver.create(path, name)
    
    @staticmethod
    def write(path: str, data: str) -> bool:
        try:
            with zip.ZipFile(path, 'a') as zf:
                zf.write(data)
                return True
        except FileExistsError:
            return False

        
    @staticmethod
    def read(path: str) -> list:
        result = []
        try:
            with zip.ZipFile(path, 'r') as zf:
                for i in zf.namelist():
                    result.append(i)
            return result
        except FileExistsError:
            return None
        
    @staticmethod
    def delete(path: str, name: str) -> bool:
        return FileDriver.delete(path, name)