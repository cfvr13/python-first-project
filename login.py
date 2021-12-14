from tkinter import * 
from tkinter.ttk import * 

root = Tk ()
root.title("login")
root.geometry("300x150")


usuario=Label(root, text="ingrese nombre de usuario")
usuario.pack()

usuario1=StringVar()
usu=Entry(root, width=30, textvariable=usuario1)
usu.pack

contraseña=Label(root, text="contraseña:")
contraseña.pack()

contra=StringVar()
contra1=Entry(root, width=30, textvariable=contra, show="*")
contra1.pack()

def ingresar(): 
    if usuario1.get ()=="cristian.viracacha" and contra.get()=="123456": 
        root.title("usuario correcto")
    else: 
        root.title("incorrecto")

bt=Button(root,text="Entrar")
bt.pack(side=BOTTOM)    

root.mainloop