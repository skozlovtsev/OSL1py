import psutil
import os
from psutil._common import bytes2human
from driver.driver import Driver
from abc import ABC, abstractmethod


class Controller(ABC):
    @abstractmethod
    def create(self) -> None:
        ...
     
    @abstractmethod
    def write(self) -> None:
        ...
    
    @abstractmethod
    def read(self) -> None:
        ...

    @abstractmethod
    def delete(self) -> None:
        ...


class FileController(Controller):
    def __init__(self, driver: Driver, postfix: str = ""):
        self.driver = driver
        self.postfix = postfix
    
    def create(self) -> None:
        fname = input("Enter filename: ")
        if self.driver.create("", fname + self.postfix):
            print("Successfully created")
            return
        print("Something went wrong")
    
    def write(self) -> None:
        path = input("Enter path: ")
        data = input("Enter data: ")
        if self.driver.write(path, data):
            return
        print("Something went wrong")
    
    def read(self) -> None:
        path = input("Enter path: ")
        data = self.driver.read(path)
        if data is None:
            print("Something went wrong")
            return
        if type(data) == list:
            for i in data:
                print(i)
            return
        print(data)
    
    def delete(self) -> None:
        fname = input("Enter filename: ")
        if self.driver.delete("", fname + self.postfix):
            print("Successfully deleted")
            return
        print("Something went wrong")


class JsonController(FileController):
    def __init__(self, driver: Driver, postfix: str = ".json"):
        self.driver = driver
        self.postfix = postfix
    
    def create(self) -> None:
        return super().create()
    
    def write(self) -> None:
        ...
    
    def read(self) -> None:
        ...
    
    def delete(self) -> None:
        return super().delete()


class FSController:
    @staticmethod
    def disk_information() -> None:
        template = "%-17s %8s %8s %8s %5s%% %9s %s"
        print(template % ("Device", "Total", "Used", "Free", "Use ", "Type",
                        "Mount"))
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue
            usage = psutil.disk_usage(part.mountpoint)
            print(template % (
                part.device,
                bytes2human(usage.total),
                bytes2human(usage.used),
                bytes2human(usage.free),
                int(usage.percent),
                part.fstype,
                part.mountpoint))