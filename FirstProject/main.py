
from tkinter import *
from tkinter.ttk import Combobox
window = Tk()

window.title("Первое окно")

a = Label(window, text="Привет", font=("Arial Bold",100))
a.grid(column = 0, row = 0)

window.geometry('1000x1000')

def clicked():

    a.configure(text =f"{e.get()}")

b = Button(window, text="00000", command=clicked, bg = "black",fg = "yellow")
b.grid(column = 0, row = 1)

e = Entry(window)
e.grid(column=0, row=2)
e1 = Entry(window)
e1.grid(column=0, row=3)
e2 = Entry(window)
e2.grid(column=0, row=4)
e.focus()

combo = Combobox(window)
combo['value'] = (1,2,3,4)
combo.grid(column=2, row=5)
window.mainloop()
