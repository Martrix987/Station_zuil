import psycopg2.extras
import psycopg2
import requests
from tkinter import *
#import datetime
api_key = "982bf4c7313a277317a3098d5fd749df"





from tkinter import *

def click_amsterdam():
    amsterdam.destroy()
    utrecht.destroy()
    leiden.destroy()
    kiezen.destroy()

    stad = 'Amsterdam'
    weerbericht(stad)

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

    berichten = Label(master=root, text='con_bericht', foreground='blue', font=('Helvetica', 16), bg='yellow',)
    berichten.pack()
    
    
    
    


    






def click_leiden():
    amsterdam.destroy()
    utrecht.destroy()
    leiden.destroy()
    kiezen.destroy()

    stad = 'Leiden'
    weerbericht(stad)

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

    berichten = Label(master=root, text='con_bericht', foreground='blue', font=('Helvetica', 16), bg='yellow',)
    berichten.pack()

    stad = 'Leiden'
    return stad


def click_utrecht():
    amsterdam.destroy()
    utrecht.destroy()
    leiden.destroy()
    kiezen.destroy()

    stad = 'Utrecht'
    weerbericht(stad)
    

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

    berichten = Label(master=root, text='con_bericht', foreground='blue', font=('Helvetica', 16), bg='yellow',)
    berichten.pack()

    stad = 'Utrecht'
    return stad




root = Tk()
root.configure(bg='yellow')
root.geometry("1080x720")
root.resizable(False, False)


kiezen = Label(
bg='yellow', master=root, text='Choose you current location', foreground='blue', font=('Helvetica', 16),)
kiezen.pack()
kiezen.place(x=450, y=260)

ns_logo = PhotoImage("ns_logo.png")
logo = Label(image=ns_logo)
logo.pack()




utrecht = Button(master=root, text='Utrecht', command=click_utrecht, foreground='blue', bg='yellow',)
utrecht.pack(pady=10)
utrecht.place(x=440, y=360)

amsterdam = Button(master=root, text='Amsterdam', command=click_amsterdam, foreground='blue', bg='yellow',)
amsterdam.pack(pady=10)
amsterdam.place(x=545, y=360)


leiden = Button(master=root, text='Leiden', command=click_leiden, foreground='blue', bg='yellow',)
leiden.pack(pady=10)
leiden.place(x=666, y=360)

def weerbericht(stad):
    tempratuur_txt = Label(master=root, text='Tempratuur in graden celcius:', foreground='blue', font=('Arial', 20), bg='yellow', )
    tempratuur_txt.pack()
    tempratuur_txt.place(x=625, y=50)  

    gevoel_txt = Label(master=root, text='Gevoels temp in graden celcius:', foreground='blue', font=('Arial', 20), bg='yellow', )
    gevoel_txt.pack()
    gevoel_txt.place(x=600, y=100)  

    vochtigheid_txt = Label(master=root, text='Luchtvochtigheid in procenten: ', foreground='blue', font=('Arial', 20), bg='yellow', )
    vochtigheid_txt.pack()
    vochtigheid_txt.place(x=616, y=150) 
    

    url = f"http://api.openweathermap.org/data/2.5/weather?q={stad}&appid={api_key}"

    weerbericht = requests.get(url).json()

    temp = weerbericht['main']['temp']
    temp = int(temp - 273.15) 
    #Omrekenen to graden celcius en int maken zodat je geen decimale krijgt

    gevoels_temp = weerbericht['main']['feels_like']
    #Omrekenen to graden celcius en int maken zodat je geen decimale krijgt
    gevoels_temp = int(gevoels_temp - 273.15) 

    luchtvochtigheid = weerbericht['main']['humidity']
    print(temp, gevoels_temp, luchtvochtigheid)

    Weersvoorspellinge = Label(master=root, text='Weersvoorspellinge:', foreground='blue', font=('Arial', 20), bg='yellow', )
    Weersvoorspellinge.pack()
    Weersvoorspellinge.place(x=735, y=0)    
    temp_amst = Label(master=root, text=temp, foreground='blue', font=('Arial', 20), bg='yellow', )
    temp_amst.pack()
    temp_amst.place(x=1000, y=50)
    gevoel_amst = Label(master=root, text=gevoels_temp, foreground='blue', font=('Arial', 20), bg='yellow',)
    gevoel_amst.pack()
    gevoel_amst.place(x=1000, y=100)
    vochtig_amst = Label(master=root, text=luchtvochtigheid, foreground='blue', font=('Arial', 20), bg='yellow',)
    vochtig_amst.pack()
    vochtig_amst.place(x=1000, y=150)  




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







