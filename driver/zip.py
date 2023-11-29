import zipfile as zip
from .file import FileDriver


class ZipDriver(FileDriver):
    @staticmethod
    def create(path: str, name: str) -> bool:
        return super().create(path, name)
    
    @staticmethod
    def write(path: str, data: str) -> bool:
        try:
            with zip.ZipFile(path, 'a') as zf:
                zf.write(data)
                return True
        except FileExistsError:
            return False

        
    @staticmethod
    def read(path: str) -> str:
        try:
            with zip.ZipFile(path, 'w') as zf:
                for i in zf.namelist():
                    with zf.open(i) as f:
                        yield f.read()
        except FileExistsError:
            return None
        
    @staticmethod
    def delete(path: str, name: str) -> bool:
        return super().delete(path, name)