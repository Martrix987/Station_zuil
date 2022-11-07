from tkinter import *
from functools import partial


root = Tk()
root.title("NS_stationsbord")

achtergrond = PhotoImage(file='station_zuil_achtergrond.png')
label = Label(
image = achtergrond,
master=root, 
text='Hello World',


)



label.pack()


root.mainloop()