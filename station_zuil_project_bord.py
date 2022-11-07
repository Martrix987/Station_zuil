import psycopg2.extras
import psycopg2
import requests
from tkinter import *
#import datetime


basis_url = "https://openweathermap.org/data/2.5/weather?" 
api_sleutel = '982bf4c7313a277317a3098d5fd749df'
stad = "Amsterdam"

url = basis_url + "appid=" + api_sleutel + "&q=" + stad

antwoord = requests.get(url).json()
print(antwoord)




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

'''
print('\n')
for berichten in non_con_bericht:
    bericht = berichten['bericht']
print(bericht)
'''



root = Tk()

achtergrond = PhotoImage(file='station_zuil_GUI_achtergrond.png')
label = Label(master=root, 
              text='Hello World', 
              background='yellow')



label.pack()


root.mainloop()








