import psycopg2.extras
import psycopg2
#import requests
from tkinter import *
#import datetime






from tkinter import *

def click_amsterdam():
    amsterdam.destroy()
    utrecht.destroy()
    leiden.destroy()
    kiezen.destroy()

    connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
    conn = psycopg2.connect(connection_string) 
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    query = """SELECT bericht, naam
                FROM bericht
                ORDER BY datumtijd_bericht DESC
                LIMIT 5;
            ;"""
    cursor.execute(query)
    non_con_bericht = cursor.fetchall()
    conn.close()
    print(non_con_bericht)

    berichten = Label(master=root, text='con_bericht', foreground='blue', font=('Helvetica', 16), height=20, bg='yellow',)
    berichten.pack()
    
    stad = 'Amsterdam'
    return stad



def click_leiden():
    amsterdam.destroy()
    utrecht.destroy()
    leiden.destroy()
    kiezen.destroy()

    connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
    conn = psycopg2.connect(connection_string) 
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    query = """SELECT bericht, naam
                FROM bericht
                ORDER BY datumtijd_bericht DESC
                LIMIT 5;
            ;"""
    cursor.execute(query)
    non_con_bericht = cursor.fetchall()
    conn.close()
    print(non_con_bericht)

    berichten = Label(master=root, text='con_bericht', foreground='blue', font=('Helvetica', 16), height=20, bg='yellow',)
    berichten.pack()

    stad = 'Leiden'
    return stad


def click_utrecht():
    amsterdam.destroy()
    utrecht.destroy()
    leiden.destroy()
    kiezen.destroy()
    

    connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
    conn = psycopg2.connect(connection_string) 
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    query = """SELECT bericht, naam
                FROM bericht
                ORDER BY datumtijd_bericht DESC
                LIMIT 5;
            ;"""
    cursor.execute(query)
    non_con_bericht = cursor.fetchall()
    conn.close()
    print(non_con_bericht)

    berichten = Label(master=root, text='con_bericht', foreground='blue', font=('Helvetica', 16), height=20, bg='yellow',)
    berichten.pack()

    stad = 'Utrecht'
    return stad




root = Tk()
root.configure(bg='yellow')
root.geometry("1080x720")
root.resizable(False, False)


kiezen = Label(
bg='yellow', master=root, text='Choose you current location', foreground='blue', font=('Helvetica', 16), height=20)
kiezen.pack()

ns_logo = PhotoImage("ns_logo.png")
logo = Label(image=ns_logo)
logo.pack()



utrecht = Button(master=root, text='Utrecht', command=click_utrecht, foreground='blue', bg='yellow',)
utrecht.pack(pady=10)
utrecht.place(x=400, y=300)

amsterdam = Button(master=root, text='Amsterdam', command=click_amsterdam, foreground='blue', bg='yellow',)
amsterdam.pack(pady=10)
amsterdam.place(x=500, y=300)


leiden = Button(master=root, text='Leiden', command=click_leiden, foreground='blue', bg='yellow',)
leiden.pack(pady=10)
leiden.place(x=625, y=300)


root.mainloop()

























'''import tkinter as tk
#from functools import partial

def onreturn(*args):
    print("amsterdam")






root = tk.Tk()
root.resizable(False, False)
root.title("NS_stationsbord")

amsterdam = tk.Entry(root)

amsterdam.bind("<return>", onreturn)

amsterdam.pack()

root.mainloop()
'''






'''
def plaats_keuze():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("NS_stationsbord")
    
    achtergrond = PhotoImage(file='station_zuil_achtergrond.png')
    label = Label(

    master=root, 
    text='Hello World',
    image = achtergrond,


    )

    Amsterdam = Button = (top,'Amsterdam')


    label.pack()


    root.mainloop()

    return plaats



plaats_keuze()




connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
query = """SELECT bericht
           FROM bericht
           ORDER BY datumtijd_bericht DESC
           LIMIT 5;
           ;"""
cursor.execute(query)
non_con_bericht = cursor.fetchall()
conn.close()

print(non_con_bericht)

print('\n')
for berichten in non_con_bericht:
    bericht = berichten['bericht']
print(bericht)




root = Tk()

achtergrond = PhotoImage(file='station_zuil_GUI_achtergrond.png')
label = Label(master=root, 
              text='Hello World', 
              background='yellow')



label.pack()


root.mainloop()
'''







