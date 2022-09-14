from tkinter import *
from tkinter import messagebox as MessageBox

def sumar():
    r.set( float(n1.get()) + float(n2.get()) )
    
    

def restar():
    r.set( float(n1.get()) - float(n2.get()) )
    


def multiplicar():
    r.set( float(n1.get()) * float(n2.get()) )


def Division():
    if(float(n2.get())==0):
        (MessageBox.showinfo("ERROR!", "No se puede dividir"))
        n1.set("")
        n2.set("")
    else:	
        r.set( float(n1.get()) / float(n2.get()))
    

def borrar():
    n1.set("")
    n2.set("")
    r.set("")

    ventana.bell()
    ventana.focus()
    
# Configuración de la raíz
ventana = Tk()
ventana.config(bd=15)
"""p = StringVar()"""
n1 = StringVar()    
n2 = StringVar()
r = StringVar()

Label(ventana, text="Número 1").pack()
caja1=Entry(ventana, justify="center", textvariable=n1).pack()


Label(ventana, text="Número 2").pack()
Entry(ventana, justify="center", textvariable=n2).pack()
"""Label(ventana, text=" ",textvariable=p).pack()
    p.set("")"""

Label(ventana, text="Resultado").pack()
Entry(ventana, justify="center", textvariable=r, state="disabled").pack()

Label(ventana, text="").pack()  # Separador

Button(ventana, text="Sumar", command=sumar).pack(side="left")
Button(ventana, text="Resta", command=restar).pack(side="left")
Button(ventana, text="Producto", command=multiplicar).pack(side="left")
Button(ventana, text="Dividir", command=Division).pack(side="left")
Button(ventana, text="Nuevo", command=borrar).pack(side="left")
     
# Finalmente bucle de la aplicación
ventana.mainloop()
