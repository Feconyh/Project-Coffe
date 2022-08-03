class Buy():
    def __init__(self):
        pass

    def purchase(self, code,who):
        path = who.Register
        check = False
        check_stock = False

        # verify if this code exists
        for i in range(len(path.listwheel)):
            if code == path.listwheel[i].code:
                check = True
                num = i

                # ask the amount
                amount = int(input('report the amount: '))

                # verify the amount
                if amount <= path.listwheel[i].amount and amount > 0:
                    check_stock = True

        # if the amount is valid and the code exists print ('thank you,...')
        if check == True and check_stock == True:
            who.list_historic(1, amount, code)
            path.listwheel[num].amount -= amount
            print('Thank you, for the purchase here')

        # if the two checks are False print ('excuse me, ...')
        if check == False or check_stock == False:
            print('excuse me, this product doesn\'t exist or we\'re out of stock')

class Sell():
    def __init__(self):
        pass

    def selling(self, code,who):
        path = who.Register
        check = False
        check_stock = False

        # verify if this code exists
        for i in range(len(path.listwheel)):
            if code == path.listwheel[i].code:
                check = True
                num = i
                
                # ask the amount
                amount = int(input('report the amount: '))

                # verify the amount
                if amount > 0:
                    check_stock = True

        # if the amount is valid and the code exists print ('thank you,...')
        if check == True and check_stock == True:
            who.list_historic(2, amount, code)
            path.listwheel[num].amount += amount
            print('Thank you, for the sale here')
        
        # if the two checks are False print ('excuse me, ...')
        if check == False or check_stock == False:
            print('excuse me, this product doesn\'t exist or this value doesn\'t valid')
