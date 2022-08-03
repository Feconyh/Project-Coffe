from control_moviment import *
from stock import *
from manufacturer import *

# class that run this program
class Run():
    def __init__(self):
        self.Stock = Stock()
        self.Buy = Buy()
        self.Sell = Sell()
        self.Manufacturer = Manufacturer()
        
    def list(self):
        exit = False
        while exit == False:
            print('\n 1 - Register'
                '\n 2 - Found Product'
                '\n 3 - Change Product Description'
                '\n 4 - Buy Product'
                '\n 5 - Sell Product'
                '\n 6 - historic'
                '\n 7 - Register Manufacturer'
                '\n 8 - Found Manufacturer'
                '\n 0 - Exit')

            decision = input('Your choice: ')

            if decision == '1':
                self.code = int(input('Which code you this product ?\n'))
                self.Stock.add_product(self.code, self.Manufacturer)

            elif decision == '2':
                self.code = input('Which code do you want ?\n')
                self.Stock.found_list(self.code)

            elif decision == '3':
                self.code = int(input('That the code of this product ?\n'))
                self.Stock.change(self.code)

            elif decision == '4':
                self.code = int(input('Report the code of the product: '))
                self.Buy.purchase(self.code,self.Stock)

            elif decision == '5':
                self.code = int(input('Report the code of the product: '))
                self.Sell.selling(self.code,self.Stock)
            
            elif decision == '6':
                self.Stock.print_historic()

            elif decision == '7':
                self.name_manufacturer = input('Report the name of manufacturer ?\n')
                self.Manufacturer.add_manufacturer(self.name_manufacturer)

            elif decision == '8':
                self.manufacturer = input('Which code do you want ?\n')
                self.Manufacturer.found_manufacturer(self.manufacturer)

            elif decision == '0':
                exit = True
                print('Good Bye')

            else:
                print('Value Invalid !')