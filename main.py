from driver.file import FileDriver
from controller import FileController, JsonController, FSController
from driver.json import JSONDriver
from driver.xml import XMLDriver
from driver.zip import ZipDriver
from menu import Menu
import sys, os

file = FileController(FileDriver)
json = JsonController(JSONDriver)
xml = JsonController(XMLDriver)
zip = FileController(ZipDriver)

main_menu = Menu([])

MENU_FILE = [["Create file", file.create], 
             ["Write string in file", file.write], 
             ["Read file", file.read], 
             ["Deleted file", file.delete], 
             ["Main menu", main_menu.print]]

MENU_JSON = [["Create JSON", json.create],  
             ["Write string in JSON", json.write],  
             ["Read JSON", json.read],  
             ["Deleted JSON", json.delete],  
             ["Main menu", main_menu.print]]

MENU_XML = [["Create XML", xml.create], 
            ["Write string in XML", xml.write], 
            ["Read XML", xml.read], 
            ["Deleted XML", xml.delete], 
            ["Main menu", main_menu.print]]

MENU_ZIP = [["Create ZIP", zip.create], 
            ["Add file in ZIP", zip.write], 
            ["Read ZIP", zip.read], 
            ["Deleted ZIP", zip.delete], 
            ["Main menu", main_menu.print]]

MAIN_MENU = [["Info about disk", FSController.disk_information], 
             ["Working with a file", Menu(MENU_FILE).print], 
             ["Working with JSON", Menu(MENU_JSON).print],
             ["Working with XML", Menu(MENU_XML).print], 
             ["Working with ZIP", Menu(MENU_ZIP).print], 
             ["Exit", sys.exit]]

def main():
    main_menu.menu = MAIN_MENU
    main_menu.print()

if __name__ == "__main__":
    main()