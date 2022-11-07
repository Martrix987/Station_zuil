from tkinter import *



root = Tk()

achtergrond = PhotoImage(file='station_zuil_achtergrond.png')
label = Label(
master=root, 
text='Hello World',
image = achtergrond


)



label.pack()


root.mainloop()