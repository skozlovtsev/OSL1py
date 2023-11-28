MAIN_MENU = [["Info about disk"], 
             ["Working with a file"], 
             ["Working with JSON"],
             ["Working with XML"], 
             ["Working with ZIP"], 
             ["Exit"]]

MENU_FILE = [["Create file"], 
             ["Write string in file"], 
             ["Read file"], 
             ["Deleted file"], 
             ["Main menu"]]

MENU_JSON = [["Create JSON"], 
             ["Write string in JSON"], 
             ["Read JSON"], 
             ["Deleted JSON"], 
             ["Main menu"]]

MENU_XML = [["Create XML"], 
            ["Write string in XML"], 
            ["Read XML"], 
            ["Deleted XML"], 
            ["Main menu"]]

MENU_ZIP = [["Create ZIP"], 
            ["Add file in ZIP"], 
            ["Read ZIP"], 
            ["Deleted ZIP"], 
            ["Main menu"]]


class Menu(object):
    def __init__(self, menu: list):
        self.menu = menu
    
    def print(self):
        for i, v in self.menu:
            print(f"{i}. {v[0]}")
        
        self.menu[int(input())][1]