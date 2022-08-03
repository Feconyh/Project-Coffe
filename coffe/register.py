from product import *

class Register():
    def __init__(self):
        self.listcount = 0
        self.listwheel = []

    def create_list(self, code, description, manufacturer, amount):
        self.listwheel.append(self.listcount)
        self.listwheel[self.listcount] = Product(code, description, manufacturer, amount)
        self.listcount += 1