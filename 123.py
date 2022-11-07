from tkinter import *
from functools import partial


root = Tk()
root.title("NS_station's_bord")

achtergrond = PhotoImage(file='station_zuil_achtergrond.png')
label = Label(
image = achtergrond,
master=root, 
text='Hello World', 
height=720,
width=1080,



)



label.pack()


root.mainloop()