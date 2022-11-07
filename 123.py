from tkinter import *



root = Tk()
root.title("NS_stationbord")


achtergrond = PhotoImage(file='station_zuil_achtergrond.png')
label = Label(
master=root, 
image = achtergrond,
text='Hello World'



)



label.pack()


root.mainloop()