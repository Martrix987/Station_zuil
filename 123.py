from tkinter import *
from functools import partial


root = Tk()

achtergrond = PhotoImage(file='station_zuil_achtergrond.png')
label = Label(
image = achtergrond,
master=root, 
text='Hello World',
image = achtergrond


)



label.pack()


root.mainloop()