class Menu(object):
    def __init__(self, menu: list):
        self.menu = menu
    
    def print(self):
        for i, v in enumerate(self.menu):
            print(f"{i}. {v[0]}")
        
        self.menu[int(input())][1]()
        self.print()