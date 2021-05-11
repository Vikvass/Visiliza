from tkinter import *

window = Tk()
c = Canvas(window, width=400, height=400, bg='#222169')
c.pack()

c.create_line(50,120,50,60,fill='white')
c.create_oval(35,30,65,60,fill='white')
c.create_line(50,90,30,60,fill='white')
c.create_line(50,90,70,60,fill='white')
c.create_line(50,120,20,130,fill='white')
c.create_line(50,120,80,130,fill='white')



window.mainloop()