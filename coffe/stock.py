from register import *

class Stock():
    def __init__(self):
        self.historic = []
        self.Register = Register()
        
    # function for add/self.Register products
    def add_product(self, code, who):
        check = False
        check_manufacturer = False
        loop = True
        for i in range(len(self.Register.listwheel)): # Run the list and verify if this code exists already
            if code == self.Register.listwheel[i].code:
                check = True

        if check == True: # if so report back to the user
            print('This code already exists')

        elif check == False: # otherwise create a new product
            print(f'Code: {code}')
            self.description = str(input('Description: '))

            while loop:
                self.manufacturer = str(input('Manufacturer: '))

                for i in who.manufacturers:
                    if i == self.manufacturer:
                        check_manufacturer = True
                        num = i

                if check_manufacturer == True:
                    loop = False
                    self.manufacturer = num

                    self.amount = int(input('Amount: '))
                    self.Register.create_list(code, self.description, self.manufacturer, self.amount)
  
                if check_manufacturer == False:
                    print('Name not exists')

                    decision = input('Name doesn\'t exist \nWant more one try ?\n')
                    if decision == 'yes':
                        loop = True
                    
                    if decision == '':
                        loop = False
                        self.manufacturer = 'No Name'

                        self.amount = int(input('Amount: '))
                        self.Register.create_list(code, self.description, self.manufacturer, self.amount)
  
    def found_list(self, code):

        if code == '':
            for i in range(len(self.Register.listwheel)):
                print(self.Register.listwheel[i])
                print('='*30)
        else:
            code = int(code)
            check = False
            num = 0
            for i in range(len(self.Register.listwheel)):
                if code == self.Register.listwheel[i].code:
                    check = True
                    num = i

            if check == True:
                print(self.Register.listwheel[num])
                
                
            elif check == False:
                print('This code doesn\'t exists')

    def change(self, code):
        check = False
        check_again = False
        for i in range(len(self.Register.listwheel)):
            if code == self.Register.listwheel[i].code:
                check = True
                num = i
                
        if check == True:
            description = input('what name you want to change ?\n')

            for i in range(len(self.Register.listwheel)):
                if description == self.Register.listwheel[i].description:
                    check_again = True
                
            if check_again == True:
                print(f'This description already exist in other')

            elif check_again == False:
                self.Register.listwheel[num].description = description
                print(f'Now this is the new product description: {self.Register.listwheel[i].description}')

        elif check == False:
            print('This code not exists')
    
    def list_historic(self, choice, amount, code):
        if choice == 1: self.historic.append(f'{amount} purchase, of product of code: {code}')
        if choice == 2: self.historic.append(f'{amount} Sell, of product of code: {code}')
        
    def print_historic(self):
        for i in range(len(self.historic)):
            print('='*17,f'{i+1}','='*17)
            print(self.historic[i])