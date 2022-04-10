from tkinter import *

radio=Tk()
radio.geometry("300x200")

R = IntVar()

def mostrar():
    if R.get()==1:
        mira.config(text="Es un Hombre")

    else:
        mira.config(text="Es una Mujer")    


Label(radio,text="Genero:",pady=20).pack()

Radiobutton(radio,text="Hombre",pady=20, variable=R,value=1,command=mostrar).pack()
Radiobutton(radio,text="Mujer",variable=R,value=2,command=mostrar).pack()

mira=Label(radio)
mira.pack()

radio.mainloop()