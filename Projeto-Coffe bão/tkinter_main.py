



from dataclasses import field
from tkinter import *




from class_compra import *

from db_estoque import *
from class_fabric import *
from class_venda import *


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

cadProd = PhotoImage(file='img/botao_produto.png')

prodbt = Button(f2,image=cadProd,bd=0,command=cadWindow)
prodbt.place(width=422, height=122, x=153, y=344)


botao_voltar = PhotoImage(file='img/voltar.png')

voltar = Button(f2, image=botao_voltar, bd=0, command=lambda: [f1.pack(), f2.pack_forget()])
voltar.place(width=62, height=89, x=53, y=23)

fabt = PhotoImage(file="img/fabricbt1.png")

fabrbt = Button(f2,image=fabt,bd=0,command=cadFabr)
fabrbt.place(width=420, height=124,x=706, y=343)

schbt = PhotoImage(file='img/searchbt1.png')

searchbt = Button(f2,image=schbt,bd=0,command=searchw)
searchbt.place(width=422, height=124, x=1274, y=344)


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
cadastrar = PhotoImage(file='img/cadastrar.png')

back3 = Label(f3,image=backg3)
back3.pack() 

voltar = Button(f3, image=botao_voltar, bd=0, command=lambda: [f2.pack(), f3.pack_forget()])
voltar.place(width=62, height=89, x=53, y=23)

botao_cadastrar = Button(f3, image=cadastrar, bd=0)
botao_cadastrar.place(width=327, height=70, x=733, y=843)

desc = Entry(f3, bd=0)
desc.config(font='Arieal 20')
desc.place(width=742, height=45, x=578, y=376)

cod = Entry(f3, bd=0)
cod.config(font='Arieal 20')
cod.place(width=742, height=45, x=578, y=500)

quant = Entry(f3, bd=0)
quant.config(font='Arieal 20')
quant.place(width=742, height=45, x=578, y=626)

#========= = = ============================= = =======[]
#========= =      =FRAME 4                        = =======[]
#========= = = ============================= = =======[]

f4 = Frame(app)


backg4 = PhotoImage(file='img/cadFabr.png')

back4 = Label(f4,image=backg4)
back4.pack()

voltar = Button(f4, image=botao_voltar, bd=0, command=lambda: [f2.pack(), f4.pack_forget()])
voltar.place(width=62, height=89, x=53, y=23)

botao_cadastrar = Button(f4, image=cadastrar, bd=0)
botao_cadastrar.place(width=335, height=77, x=738, y=842)

fabr = Entry(f4, bd=0)
fabr.config(font='Arieal 20')
fabr.place(width=742, height=45, x=654, y=505)


#========= = = ============================= = =======[]
#========= =      =FRAME 5                         = =======[]
#========= = = ============================= = =======[]

f5 = Frame(app)


backg5 = PhotoImage(file='img/search.png')


back5 = Label(f5,image=backg5)
back5.pack()


imgsearch = PhotoImage(file='img/codigo_produtobt.png')


voltar = Button(f5, image=botao_voltar, bd=0, command=lambda: [f2.pack(), f5.pack_forget()])
voltar.place(width=62, height=89, x=53, y=23)




procbt = Button(f5,image=imgsearch,bd=0)
procbt.place(width=380, height=75, x=226, y=335)

proc = Entry(f5, bd=0)
proc.config(font='Arieal 20')
proc.place(width=742, height=45, x=679, y=356)


#========= = = ============================= = =======[]
#========= =      =FRAME 6                         = =======[]
#========= = = ============================= = =======[]

f6 = Frame(app)


backg6 = PhotoImage(file='img/alter.png')

alterar = PhotoImage(file='img/alterar.png')


back6 = Label(f6,image=backg6)
back6.pack()

voltar = Button(f6, image=botao_voltar, bd=0, command=lambda: [f2.pack(), f6.pack_forget()])
voltar.place(width=62, height=89, x=53, y=23)

botao_alterar = Button(f6, image=alterar, bd=0)
botao_alterar.place(width=313, height=74, x=747, y=841)

codp = Entry(f6, bd=0)
codp.config(font='Arieal 20')
codp.place(width=742, height=45, x=649, y=461)

descp = Entry(f6, bd=0)
descp.config(font='Arieal 20')
descp.place(width=742, height=45, x=649, y=590)

#========= = = ============================= = =======[]
#========= =      =FRAME 7                         = =======[]
#========= = = ============================= = =======[]
f7 = Frame(app)

backg7 = PhotoImage(file='img/excluir.png')

excluirimg = PhotoImage(file='img/excluirBt.png')

back7 = Label(f7, image=backg7)
back7.pack()

voltar = Button(f7, image=botao_voltar, bd=0, command=lambda: [f2.pack(), f7.pack_forget()])
voltar.place(width=62, height=89, x=53, y=23)

botao_excluir = Button(f7, image=excluirimg, bd=0)
botao_excluir.place(width=315, height=77, x=746, y=838)

excluir = Entry(f7, bd=0)
excluir.config(font='Arieal 20')
excluir.place(width=742, height=45, x=648, y=460)

app.mainloop()