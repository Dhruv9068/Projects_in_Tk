from tkinter import *
from tkinter.ttk import *
from time import strftime

top = Tk()
top.title("Digital clock")



def update_time():
    text = strftime(' %H:%M:%S %p')
    lbl.config(text=text)
    lbl.after(1000, update_time)
lbl = Label(top, font=('digital-7', 50, 'bold'), background='black', foreground='red' )
lbl.pack(anchor='center')

update_time()
top.mainloop()
