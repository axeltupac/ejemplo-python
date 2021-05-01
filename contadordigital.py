from tkinter import *
contador= 0
def contDig(nombre:Label):
    contador= 0
    def digito ():
        global contador
        contador = contador + 1
        nombre.config(text=str(contador))
        nombre.after(100, digito)
    digito()
root= Tk()
root.title ('contador digital')
nombre= Label(fg='blue', font= 50)
nombre.pack()
contDig(nombre)
boton= Button (text='Finalizar', width= 50, command=root.destroy)
boton.pack()








root.mainloop()