from tkinter import *
from tkinter.colorchooser import *

root= Tk ()
root.geometry('250x100')
def micolor ():
    color=askcolor ()
    nomb= Label (text='Este es tu color elegido', bg= color[1]).pack()
    print (color)

boton= Button (text= ('elegi el color'), command= micolor).pack()




root.mainloop()