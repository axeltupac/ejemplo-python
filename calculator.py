from tkinter  import *
import tkinter.messagebox
def botones (numeros):
    global operador
    operador = operador + str (numeros)
    txt_input.set(operador)
def limpiar () :
    global operador
    operador = ''
    txt_input.set('')
    Display.insert (0 ,'Empeza a calcular...' )
def igual() :
    global operador
    total=  float (eval (operador))
    txt_input.set(total)
    #operador= ''
def mensajeGuardar():
    tkinter.messagebox.showinfo('Guardar', '¿Desea guardar este archivo?')
def mensajeEliminar():
    tkinter.messagebox.askquestion('Eliminar' , '¿Desea Eliminar este archivo?')
root = Tk()
root.title ('Calculadora')

operador = ''
txt_input= StringVar (value= 'Empeza a calcular...')
#============Pantalla=========================
Display = Entry(root,font = ('arial' , 30 , 'bold'), fg= 'white', bg='blue', justify ='right' , bd= 50, textvariable=txt_input)
Display.grid(columnspan=4)


#===============Fila1================================
boton7= Button (root, padx=30, pady=15, bd=8, fg = 'blue', font =('arial', 30, 'bold'), text= '7', command= lambda:botones(7)).grid (row=1, column=0)
boton8= Button (root, padx=30, pady=15, bd=8, fg = 'blue', font =('arial', 30, 'bold'), text= '8',command= lambda:botones(8)).grid (row=1, column=1)
boton9= Button (root, padx=30, pady=15, bd=8, fg = 'blue', font =('arial', 30, 'bold'), text= '9',command= lambda:botones(9)).grid (row=1, column=2)
botonC= Button (root, padx=30, pady=15, bd=8, fg = 'black', font =('arial', 30, 'bold'), text= 'C', bg= 'dark grey', command=limpiar).grid (row=1, column=3)

#==============Fila2==================================
boton4= Button (root, padx=30, pady=15, bd=8, fg = 'blue', font =('arial', 30, 'bold'), text= '4',command= lambda:botones(4)).grid (row=2, column=0)
boton5= Button (root, padx=30, pady=15, bd=8, fg = 'blue', font =('arial', 30, 'bold'), text= '5',command= lambda:botones(5)).grid (row=2, column=1)
boton6= Button (root, padx=30, pady=15, bd=8, fg = 'blue', font =('arial', 30, 'bold'), text= '6',command= lambda:botones(6)).grid (row=2, column=2)
botonSuma= Button (root, padx=33, pady=15, bd=8, fg = 'black', font =('arial', 30, 'bold'), text= '+', bg= 'grey',command= lambda:botones('+')).grid (row=2, column=3)




#==========================Fila3==========================
boton1= Button (root, padx=30, pady=15, bd=8, fg = 'blue', font =('arial', 30, 'bold'), text= '1',command= lambda:botones(1)).grid (row=3, column=0)
boton2= Button (root, padx=30, pady=15, bd=8, fg = 'blue', font =('arial', 30, 'bold'), text= '2',command= lambda:botones(2)).grid (row=3, column=1)
boton3= Button (root, padx=30, pady=15, bd=8, fg = 'blue', font =('arial', 30, 'bold'), text= '3',command= lambda:botones(3)).grid (row=3, column=2)
botonResta= Button (root, padx=38, pady=15, bd=8, fg = 'black', font =('arial', 30, 'bold'), text= '-', bg= 'grey',command= lambda:botones('-')).grid (row=3, column=3)


#===========================Fila4==============================================
boton0= Button (root, padx=30, pady=15, bd=8, fg = 'blue', font =('arial', 30, 'bold'), text= '0', command= lambda:botones(0) ).grid (row=4, column=0)
botonPunto= Button (root, padx=35, pady=15, bd=8, fg = 'black', font =('arial', 30, 'bold'), text= '.', bg= 'grey',command= lambda:botones('.')).grid (row=4, column=1)
botonDiv= Button (root, padx=36, pady=15, bd=8, fg = 'black', font =('arial', 30, 'bold'), text= '/', bg= 'grey',command= lambda:botones('/')).grid (row=4, column=2)
botonMul= Button (root, padx=36, pady=15, bd=8, fg = 'black', font =('arial', 30, 'bold'), text= '*', bg= 'grey',command= lambda:botones('*')).grid (row=4, column=3)


#=========================Fila5=================================
botonIgual= Button (root, padx=95, pady=15, bd=8, fg = 'black', font =('arial', 30, 'bold'), text= '=', bg= 'grey', command=igual).grid (row=5, column=0, columnspan=2)
botonAbreParentesis= Button (root, padx=35, pady=15, bd=8, fg = 'black', font =('arial', 30, 'bold', ), text= '(', bg= 'grey',command= lambda:botones('(')).grid (row=5, column=2)
botonCierraParentesis= Button (root, padx=38, pady=15, bd=8, fg = 'black', font =('arial', 30, 'bold'), text= ')', bg= 'grey',command= lambda:botones(')')).grid (row=5, column=3)



root.mainloop()