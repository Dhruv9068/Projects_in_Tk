
from tkinter import*

window=Tk()
c=Canvas(window,width=500, height=500)
c.pack()


c.create_line(500,500,0,0,width=5,fill='Green')
c.create_line(0,500,500,0,width=5,fill='blue',dash='3')
mainloop()

