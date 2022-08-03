from manufacturer import *

# class Product
class Product():
    def __init__(self, code, description, manufacturer, amount):
        self.code = code
        self.description = description
        self.manufacturer = manufacturer
        self.amount = amount

    def __str__(self):
        info = (f'{self.code}, {self.description}, {self.manufacturer}, {self.amount}')
        return info
