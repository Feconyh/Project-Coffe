
from dataclasses import field
from email.mime import image
from math import fabs
from tkinter import *
from tkinter import messagebox
from time import *
from turtle import color


from class_compra import *

from db_estoque import *
from class_fabric import *
from class_venda import *

from setuptools import Command
from img import *
import posiciona




"""
def saveEmp():
    fabr = Fabric()
    nomEmpr = empEntry.get()
    fabr.cadastro_fabric(nomEmpr)
    infm = messagebox.showinfo(title='Nice Broh.', message='Empresa cadastrada com Sucesso!!')
    f2.forget()
    f1.pack()


def saveProd():
    Estq = Db_estoque()
    nomeProd = entrynom.get()
    nomeEmp = entryEmp.get()
    Estq.cadastrar_produto(nomeProd,nomeEmp)
    if  Estq.verifyx ==True :
        infm = messagebox.showinfo(title='Nice Broh.', message='Produto  cadastrado com Sucesso!!')
        f3.forget()
        f1.pack()
    else:
        infm = messagebox.showerror(title='Nice Broh.', message='Empresa inexistente')
    


def cadProd():
    f1.forget()
    f3.pack()


def cadEmp():
    f1.forget()
    f2.pack()


def buySell():
    f1.forget()
    f4.pack()


def returnMenu():
    f4.forget()
    f1.pack()


def view():
    f1.forget()
    f5.pack()


def returnview():
    frameedit.place_forget()
    f5.forget()
    f1.pack()


def search():
    Estq = Db_estoque()
    a = searchCode.get()
    db = Estq.listar_unidade(a)
    if a != '':
        unityinfo.insert(END, db)
    else:
        for y in range(len(Estq.pls)):
            print(len(Estq.pls))
            unityinfo.insert(END, Estq.pls[y])



def openBuy():
    f4.forget()
    f6.pack()


def returnBuy():
    minif6.place_forget()
    f6.forget()
    f4.pack()

def buyverify():
    cp = Compra()
    a = entryBuy.get()
    print(a)
    cp.comprar(a)
    print(cp.verifyy)
    if cp.verifyy == True:
       minif6.place(width=411, height=157, x=131, y=259)
       

def buyconfirm():
    cp = Compra()
    verifccod = entryBuy.get()
    q = int(entryQuan.get())
    cp.quanbuy(cod = verifccod,quan = q)
    

    
def clear():
    unityinfo.delete(0,END)
      
        

def editName():
    frameedit.place(width=125, height=210, x=516, y=343)
    
def updateName():
    db = Db_estoque()
    codeT = entryminicode.get()
    name = entryNewName.get()
    db.update_produto(code = codeT,new_name = name)
    infm = messagebox.showinfo(title='Nice Broh.', message=f'Nome alterado com Sucesso!..Codigo do produto:{codeT}|Novo:{name}')



def openSell():
    f4.forget()
    f7.pack()



def returnSell():
    minif7.place_forget()
    f7.forget()
    f4.pack()



def sellVerify():
    vd = Venda()
    a = entrySell.get()
    print(a)
    vd.vender(a)
    if vd.verifyy == True:
       minif7.place(width=411, height=157, x=131, y=259)
       

def sellconfirm():
    vd = Venda()
    verifccod = entrySell.get()
    qs = entryQuanti.get()
    vd.quanSell(cod = verifccod,quan = qs)
    


"""

def startMenu():
  f1.forget()
  f2.pack()


def cadWindow():
    f2.forget()
    f3.pack()


def cadFabr():
    f2.forget()
    f4.pack()

def searchw():
    f2.forget()
    f5.pack()

def alterw():
    f2.forget()
    f6.pack()


def delp():
    f2.forget()
    f7.pack()


app = Tk()
app.geometry('1920x1080')
app.resizable(width=False, height=False)
app.title('Café do Bão')
app.configure(bg='black')




app.bind('<Button-1>', posiciona.inicio_place)
app.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, app))
app.bind('<Button-2>', lambda arg: posiciona.para_geometry(app))






#================- = ================================== = ===============================


#======================================================================================





#========= = = ============================= = =======[]
#========= =      =FRAME 1                         = =======[]
#========= = = ============================= = =======[]



f1 = Frame(app)
f1.pack()



phot1 = PhotoImage(file="img/menu.png")


back1 = Label(f1,image=phot1)
back1.pack()



btn1 =  PhotoImage(file="img/btn1.png")

btn = Button(f1,image=btn1,bd=0,command=startMenu)
btn.place(width=424, height=128, x=682, y=487)



#========= = = ============================= = =======[]
#========= =      =FRAME 2                         = =======[]
#========= = = ============================= = =======[]



f2 = Frame(app)

backg2 = PhotoImage(file="img/lmenu.png")

back2 = Label(f2,image=backg2)
back2.pack()

cadProd = PhotoImage(file='img/prodbt1.png')

prodbt = Button(f2,image=cadProd,bd=0,command=cadWindow)
prodbt.place(width=420, height=124, x=155, y=344)



fabt = PhotoImage(file="img/fabricbt1.png")

fabrbt = Button(f2,image=fabt,bd=0,command=cadFabr)
fabrbt.place(width=420, height=124,x=706, y=343)

schbt = PhotoImage(file='img/searchbt1.png')

searchbt = Button(f2,image=schbt,bd=0,command=searchw)
searchbt.place(width=420, height=124, x=1294, y=343)


altrbt = PhotoImage(file="img/alterprodbt1.png")

altbt = Button(f2,image=altrbt,bd=0,command=alterw)
altbt.place(width=420, height=124, x=383, y=591)

delimg = PhotoImage(file="img/delbt1.png")

delbt = Button(f2,image=delimg,bd=0,command=delp)
delbt.place(width=420, height=124, x=1021, y=592)



#========= = = ============================= = =======[]
#========= =      =FRAME 3                         = =======[]
#========= = = ============================= = =======[]

f3 = Frame(app)

backg3 = PhotoImage(file="img/cadProdt.png")


back3 = Label(f3,image=backg3)
back3.pack() 





#========= = = ============================= = =======[]
#========= =      =FRAME 4                        = =======[]
#========= = = ============================= = =======[]

f4 = Frame(app)


backg4 = PhotoImage(file='img/cadFabr.png')


back4 = Label(f4,image=backg4)
back4.pack()





#========= = = ============================= = =======[]
#========= =      =FRAME 5                         = =======[]
#========= = = ============================= = =======[]

f5 = Frame(app)


backg5 = PhotoImage(file='img/search.png')


back5 = Label(f5,image=backg5)
back5.pack()




#========= = = ============================= = =======[]
#========= =      =FRAME 6                         = =======[]
#========= = = ============================= = =======[]

f6 = Frame(app)


backg6 = PhotoImage(file='img/alter.png')


back6 = Label(f6,image=backg6)
back6.pack()


#========= = = ============================= = =======[]
#========= =      =FRAME 7                         = =======[]
#========= = = ============================= = =======[]
f7 = Frame(app)


backg7 = PhotoImage(file='img/delprod.png')


back7 = Label(f7,image=backg7)
back7.pack()



app.mainloop()