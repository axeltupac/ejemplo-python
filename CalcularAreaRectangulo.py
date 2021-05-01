from tkinter import *
root= Tk()
root.title('Area de un Rectangulo')
def CalcularArea():
    al= alt.get()
    la=lar.get()
    total= la*al
    Area.insert (0, total)
def eliminar():
    altura.delete(0 , END)
    largo.delete(0, END)
    Area.delete(0,END)
alt= IntVar()
lar= IntVar()
Label(text='Area de un Rectangulo' ,padx=10 , font=('calibri' , 30, 'bold')).grid(row= 0 , column=1)


Label(text='Altura' ,padx=10 , font=('calibri' , 30, 'bold')).grid(row= 1 , sticky=W)
altura= Entry (width=30,font=('calibri' , 30, 'bold'), textvariable=alt)
altura.grid(row=1, column=1)


Label(text='Largo' ,padx=10 , font=('calibri' , 30, 'bold')).grid(row= 2 , sticky=W)
largo= Entry (width= 30,font=('calibri' , 30, 'bold'), textvariable=lar)
largo.grid(row=2 , column=1)

Label(text='Area' ,padx=10 , font=('calibri' , 30, 'bold')).grid(row= 3 , sticky=W)
Area= Entry (width=30,font=('calibri' , 30, 'bold'))
Area.grid(row=3, column=1)

Button(text='Calcular', font=('calibri' , 30, 'bold'),width=15, command=CalcularArea).grid(row=4, column=1, sticky=W)
Button(text='Limpar', font=('calibri' , 30, 'bold'), width=15, command=eliminar).grid(row=4, column=1, sticky= E)

root.mainloop()