class Manufacturer():
    def __init__(self):
        self.manufacturers = []

    def add_manufacturer(self,new):
        self.manufacturers.append(new)

    def found_manufacturer(self, manufacturer):

        if manufacturer == '':
            for i in range(len(self.manufacturers)):
                print(self.manufacturers[i])
                print('='*30)
        else:
            check = False
            num = 0
            for i in range(len(self.manufacturers)):
                if manufacturer == self.manufacturers[i]:
                    check = True
                    num = i

            if check == True:
                print('Manufacturer found:\n',self.manufacturers[num])
                
            elif check == False:
                print('This manufacturers doesn\'t exists')