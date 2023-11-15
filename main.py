from driver.file import FileDriver
from driver.fs import disk_information
from driver.json import JSONDriver
from driver.xml import XMLDriver
from driver.zip import ZipDriver
import sys, os



MAIN_MENU = ["Info about disk", "Working with a file", "Working with JSON",
            "Working with XML", "Working with ZIP", "Exit"]

MENU_FILE = ["Create file", "Write string in file", "Read file", "Deleted file", "Main menu"]

MENU_JSON = ["Create JSON", "Write string in JSON", "Read JSON", "Deleted JSON", "Main menu"]

MENU_XML = ["Create XML", "Write string in XML", "Read XML", "Deleted XML", "Main menu"]

MENU_ZIP = ["Create ZIP", "Add file in ZIP", "Read ZIP", "Deleted ZIP", "Main menu"]

def main():
    main_menu()

def print_menu(argc):
    for i in range(len(argc)):
        print(i + 1, " " + argc[i])


def work(menu, switch):
    print_menu(menu)
    choose(len(menu), switch)

def work_with_file():
    work(MENU_FILE, switch_work_with_files)


def work_with_json():
    work(MENU_JSON, switch_work_with_json)


def work_with_xml():
    work(MENU_XML, switch_work_with_xml)


def work_with_zip():
    work(MENU_ZIP, switch_work_with_zip)


def main_menu():
    print_menu(MAIN_MENU)
    choose(len(MAIN_MENU), switch_main_menu)
    


def choose(count_action, func):
    flag = True
    while flag:
        try:
            print("Action = ", end="")
            number_action = int(input())
            flag = False
        except Exception:
            print('Wrong number')
    if number_action <= count_action:
        try:
            print("_" * 100)
            func(number_action)()
            print("_" * 100)
            choose(count_action, func)
        except KeyError as e:
            raise ValueError('Undefined unit: {}'.format(e.args[0]))


def switch_main_menu(value):
    return {
        1: disk_information,
        2: work_with_file,
        3: work_with_json,
        4: work_with_xml,
        5: work_with_zip,
        6: sys.exit
    }.get(value)

def switch_work_with_files(value):
    return {
        1: FileDriver.create(path = os.getcwd(), name = str(input("Name of file: "))),
        2: FileDriver.write(path = os.getcwd(), data = str(input("Write data: "))),
        3: FileDriver.read(path = os.getcwd() + "/" + str(input("Name of file: "))),
        4: FileDriver.delete(path = os.getcwd(), name = str(input("Name of file: "))),
        5: main_menu
    }.get(value)

def switch_work_with_json(value):
    return {
        1: JSONDriver.create(path = os.getcwd(), name = str(input("Name of JSONfile: "))),
        2: JSONDriver.write(path = os.getcwd() + "/" + str(input("Name of JSONfile: ")), data = list(input("Write data: ")) | dict(input("Write data: "))),
        3: JSONDriver.read(path = os.getcwd() + "/" + str(input("Name of JSONfile: "))),
        4: JSONDriver.delete(path = os.getcwd(), name = str(input("Name of JSONfile: "))),
        5: main_menu
    }.get(value)

def switch_work_with_xml(value):
    return {
        1: XMLDriver.create(path = os.getcwd(), name = str(input("Name of XMLfile: "))),
        2: XMLDriver.write(path = os.getcwd() + "/" + str(input("Name of XMLfile: ")), data = list(input("Write data: ")) | dict(input("Write data: "))),
        3: XMLDriver.read(path = os.getcwd() + "/" + str(input("Name of XMLfile: "))),
        4: XMLDriver.delete(path = os.getcwd(), name = str(input("Name of XMLfile: "))),
        5: main_menu
    }.get(value)

def switch_work_with_zip(value):
    return {
        1: ZipDriver.create(path = os.getcwd(), name = str(input("Name of Zipfile: "))),
        2: ZipDriver.write(path = os.getcwd(), data = str(input("Write data: "))),
        3: ZipDriver.read(path = os.getcwd() + "/" + str(input("Name of Zipfile: "))),
        4: ZipDriver.delete(path = os.getcwd(), name = str(input("Name of Zipfile: "))),
        5: main_menu
    }.get(value)

if __name__ == "__main__":
    main()