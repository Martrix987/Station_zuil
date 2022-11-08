import psycopg2.extras
import psycopg2
import requests
import tkinter
from tkinter import *
api_key = "982bf4c7313a277317a3098d5fd749df"
#benodigheden worden geinporteerd en api_key is nodig voor het weer


#indien knop amsterdam wordt gedrukt worden alle knoppen en tekst verwijderd behalve het NS logo
#en worden de beibehorden functies aangeroepen
#weerbericht en voorzieningen hebben de locatie nodig
#dit gebeurd voor alle 3 de functies
def click_amsterdam():
    amsterdam.destroy()
    utrecht.destroy()
    leiden.destroy()
    kiezen.destroy()

    stad = 'Amsterdam'
    weerbericht(stad)
    voorzieningen(stad)
    berichten()
   
 

def click_leiden():
    amsterdam.destroy()
    utrecht.destroy()
    leiden.destroy()
    kiezen.destroy()

    stad = 'Leiden'
    weerbericht(stad)
    voorzieningen(stad)
    berichten()
    


def click_utrecht():
    amsterdam.destroy()
    utrecht.destroy()
    leiden.destroy()
    kiezen.destroy()

    stad = 'Utrecht'
    weerbericht(stad)
    voorzieningen(stad)
    berichten()



#de basis voor de GUI word aangeroepen (formaat, achtergrond, formaataanpasbaar False)
root = Tk()
root.configure(bg='yellow')
root.geometry("1080x720")
root.resizable(False, False)

#label met de tekst keizen voor de buttons
kiezen = Label(master=root, bg='yellow', text='Choose you current location', foreground='blue', font=('Helvetica', 16),)
kiezen.pack()
kiezen.place(x=450, y=260)

#ns logo plaatje
img = PhotoImage(file='ns_logo.png')
ns_logo = Label(root, image=img, bg='yellow')
ns_logo.pack()
ns_logo.place(x=0, y=0)

#Hier worden de foto's voor de facaliteiten alvast aangeroepen
img_ov_fiets = PhotoImage(file='img_ovfiets.png')
ov_fiets_logo = Label(master = root, image=img_ov_fiets, bg='yellow')

img_lift = PhotoImage(file='img_lift.png')
lift_logo = Label(master = root, image=img_lift, bg='yellow')

img_toilet = PhotoImage(file='img_toilet.png')
wc_logo = Label(master = root, image=img_toilet, bg='yellow')

img_pr = PhotoImage(file='img_pr.png')
laaden_lossen_logo = Label(master = root, image=img_pr, bg='yellow')


#button om te kiezen of je in: Amsterdam, Utrecht of Leiden station bent
utrecht = Button(master=root, text='Utrecht', command=click_utrecht, foreground='blue', bg='yellow',)
utrecht.pack(pady=10)
utrecht.place(x=440, y=360)

amsterdam = Button(master=root, text='Amsterdam', command=click_amsterdam, foreground='blue', bg='yellow',)
amsterdam.pack(pady=10)
amsterdam.place(x=545, y=360)

leiden = Button(master=root, text='Leiden', command=click_leiden, foreground='blue', bg='yellow',)
leiden.pack(pady=10)
leiden.place(x=666, y=360)


#functie om de berichten te zien
def berichten():
    #opvragen uit de DB van de 5 meest recenten berichten 
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

#elk bericht en naam wordt uit de library gehaald en in de variable naam[getal].txt gezet
    naam1 = non_con_bericht[0]['naam']
    naam2 = non_con_bericht[1]['naam']
    naam3 = non_con_bericht[2]['naam']
    naam4 = non_con_bericht[3]['naam']
    naam5 = non_con_bericht[4]['naam']

    bericht1 = non_con_bericht[0]['bericht']
    bericht2 = non_con_bericht[1]['bericht']
    bericht3 = non_con_bericht[2]['bericht']
    bericht4 = non_con_bericht[3]['bericht']
    bericht5 = non_con_bericht[4]['bericht']

#en de layaout van de labels waarin de berichten worden weergegeven (omstebeurd: naam bericht)
    naam_berichten_txt = Label(master=root, text='Naam en berichten van onze gebruiker: ', foreground='black', font=('Arial', 12), bg='white',)
    naam_berichten_txt.place(x=0, y=175)

    naam1_txt = Label(master=root, text=naam1, foreground='black', font=('Arial', 8), bg='white',)
    naam1_txt.place(x=0, y=200)
    bericht1_txt = Label(master=root, text=bericht1, foreground='black', font=('Arial', 7), bg='white',)
    bericht1_txt.place(x=0, y=225)

    naam2_txt = Label(master=root, text=naam2, foreground='black', font=('Arial', 8), bg='white',)
    naam2_txt.place(x=0, y=250)
    bericht2_txt = Label(master=root, text=bericht2, foreground='black', font=('Arial', 7), bg='white',)
    bericht2_txt.place(x=0, y=275)

    naam3_txt = Label(master=root, text=naam3, foreground='black', font=('Arial', 8), bg='white',)
    naam3_txt.place(x=0, y=300)
    bericht3_txt = Label(master=root, text=bericht3, foreground='black', font=('Arial', 7), bg='white',)
    bericht3_txt.place(x=0, y=325)

    naam4_txt = Label(master=root, text=naam4, foreground='black', font=('Arial', 8), bg='white',)
    naam4_txt.place(x=0, y=350)
    bericht4_txt = Label(master=root, text=bericht4, foreground='black', font=('Arial', 7), bg='white',)
    bericht4_txt.place(x=0, y=375)

    naam5_txt = Label(master=root, text=naam5, foreground='black', font=('Arial', 8), bg='white',)
    naam5_txt.place(x=0, y=400)
    bericht5_txt = Label(master=root, text=bericht5, foreground='black', font=('Arial', 7), bg='white',)
    bericht5_txt.place(x=0, y=425)



    




#de functie voor het weerbericht bestaat uit een label voor tempratuur, gevoels tempratuur en luchtvochtigheid
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
    
#hier word de API weerbericht geopend en uitgelezen met de API key en de stad van de geklikte button
    url = f"http://api.openweathermap.org/data/2.5/weather?q={stad}&appid={api_key}"
    weerbericht = requests.get(url).json()

#Hier wordt de info gehaald uit de library van het weerbericht en naar grade celuis omgerekend en in een integer gezet (zodat geen deciamle)
    temp = weerbericht['main']['temp']
    temp = int(temp - 273.15) 

#Hier wordt de info gehaald uit de library van het weerbericht en naar grade celuis omgerekend en in een integer gezet (zodat geen deciamle)
    gevoels_temp = weerbericht['main']['feels_like']
    gevoels_temp = int(gevoels_temp - 273.15) 

#Hier wordt de info gehaald uit de library van het weerbericht
    luchtvochtigheid = weerbericht['main']['humidity']

#het weerbericht wordt in de GUI gezet met labels
    Weersvoorspellinge = Label(master=root, text='Weersvoorspellinge:', foreground='blue', font=('Arial', 20), bg='yellow', )
    Weersvoorspellinge.place(x=735, y=0)    
    temp = Label(master=root, text=temp, foreground='blue', font=('Arial', 20), bg='yellow', )
    temp.place(x=1000, y=50)
    gevoel = Label(master=root, text=gevoels_temp, foreground='blue', font=('Arial', 20), bg='yellow',)
    gevoel.place(x=1000, y=100)
    vochtig = Label(master=root, text=luchtvochtigheid, foreground='blue', font=('Arial', 20), bg='yellow',)
    vochtig.place(x=1000, y=150)  


#in deze functie wordt gekeken welke stad de persoon heeft aangeclikt en dan wordt uit de DB de facaliteiten van dat station uitgelezen
def voorzieningen(stad):
    connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
    conn = psycopg2.connect(connection_string) 
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cursor.execute("SELECT   ov_fiets, lift, wc, laaden_lossen   FROM station_service   WHERE station_stad = %s", (stad,))

    voorzieningen = cursor.fetchall()
    conn.close()
    print(voorzieningen)
    ov_fiets = voorzieningen[0]['ov_fiets']
    lift = voorzieningen[0]['lift']
    wc = voorzieningen[0]['wc']
    laaden_lossen = voorzieningen[0]['laaden_lossen']

#De layout voor de voorzieningen wordt hier gedeeltelijk vastgelegd
    voorzieningen_txt = Label(master=root, text='De pictogrammen hieronder \nstaan voor de aanwezig faciliteiten op dit station: ', foreground='blue', font=('Arial', 20), bg='yellow', )
    voorzieningen_txt.pack()
    voorzieningen_txt.place(x=450, y=500)

#op regel 68 totenmet ongeveer regel 80 word het eerste gedeelte van de foto aangeroepen.
#hier wordt slechts layout gemaakt voor de foto's
    if ov_fiets == True:
        ov_fiets = Label(image = img_ov_fiets)
        ov_fiets_logo.pack()
        ov_fiets_logo.place(x=700, y=590)

    if lift == True:
        lift = Label(image = img_lift)
        lift_logo.pack()
        lift_logo.place(x=400, y=590)

    if wc == True:
        wc = Label(image = img_toilet)
        wc_logo.pack()
        wc_logo.place(x=550, y=590)

    if laaden_lossen == True:
        laaden_lossen = Label(image = img_pr)
        laaden_lossen_logo.pack()
        laaden_lossen_logo.place(x=875, y=590)
 






root.mainloop()























