import psycopg2.extras
import psycopg2
import requests
import tkinter
from tkinter import *
from PIL import ImageTk, Image

api_key = "982bf4c7313a277317a3098d5fd749df"


def click_amsterdam():
    amsterdam.destroy()
    utrecht.destroy()
    leiden.destroy()
    kiezen.destroy()

    stad = 'Amsterdam'
    weerbericht(stad)
    berichten()
    voorzieningen(stad)
 

def click_leiden():
    amsterdam.destroy()
    utrecht.destroy()
    leiden.destroy()
    kiezen.destroy()

    stad = 'Leiden'
    weerbericht(stad)
    berichten()
    voorzieningen(stad)


def click_utrecht():
    amsterdam.destroy()
    utrecht.destroy()
    leiden.destroy()
    kiezen.destroy()

    stad = 'Utrecht'
    weerbericht(stad)
    voorzieningen(stad)
    berichten()




root = Tk()
root.configure(bg='yellow')
root.geometry("1080x720")
root.resizable(False, False)

kiezen = Label(master=root, bg='yellow', text='Choose you current location', foreground='blue', font=('Helvetica', 16),)
kiezen.pack()
kiezen.place(x=450, y=260)

img = PhotoImage(file='ns_logo.png')
ns_logo = Label(root, image=img, bg='yellow')
ns_logo.pack()
ns_logo.place(x=0, y=0)


img_ov_fiets = PhotoImage(file='img_ovfiets.png')
ov_fiets_logo = Label(master = root, image=img_ov_fiets, bg='yellow')

img_lift = PhotoImage(file='img_lift.png')
lift_logo = Label(master = root, image=img_lift, bg='yellow')

img_toilet = PhotoImage(file='img_toilet.png')
wc_logo = Label(master = root, image=img_toilet, bg='yellow')

img_pr = PhotoImage(file='img_pr.png')
laaden_lossen_logo = Label(master = root, image=img_pr, bg='yellow')





utrecht = Button(master=root, text='Utrecht', command=click_utrecht, foreground='blue', bg='yellow',)
utrecht.pack(pady=10)
utrecht.place(x=440, y=360)

amsterdam = Button(master=root, text='Amsterdam', command=click_amsterdam, foreground='blue', bg='yellow',)
amsterdam.pack(pady=10)
amsterdam.place(x=545, y=360)


leiden = Button(master=root, text='Leiden', command=click_leiden, foreground='blue', bg='yellow',)
leiden.pack(pady=10)
leiden.place(x=666, y=360)




def berichten():
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

    Weersvoorspellinge = Label(master=root, text='Weersvoorspellinge:', foreground='blue', font=('Arial', 20), bg='yellow', )
    Weersvoorspellinge.pack()
    Weersvoorspellinge.place(x=735, y=0)    
    temp = Label(master=root, text=temp, foreground='blue', font=('Arial', 20), bg='yellow', )
    temp.pack()
    temp.place(x=1000, y=50)
    gevoel = Label(master=root, text=gevoels_temp, foreground='blue', font=('Arial', 20), bg='yellow',)
    gevoel.pack()
    gevoel.place(x=1000, y=100)
    vochtig = Label(master=root, text=luchtvochtigheid, foreground='blue', font=('Arial', 20), bg='yellow',)
    vochtig.pack()
    vochtig.place(x=1000, y=150)  



def voorzieningen(stad):
    connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
    conn = psycopg2.connect(connection_string) 
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cursor.execute("SELECT   ov_fiets, lift, wc, laaden_lossen   FROM station_service   WHERE station_stad = %s", (stad,))

    voorzieningen = cursor.fetchall()
    conn.close()
    print(voorzieningen)
    #gaat hier iets fout want in voorzieningen staat true fals true false maar na de for loop word fals true fals true
    for berichten in voorzieningen:
        ov_fiets = berichten[berichten[0]]
        lift = berichten[berichten[1]]
        wc = berichten[berichten[2]]
        laaden_lossen = berichten[berichten[3]]
    print(ov_fiets)
    print(lift)
    print(wc)
    print(laaden_lossen)

    voorzieningen_txt = Label(master=root, text='De pictogrammen hieronder \nstaan voor de aanwezig faciliteiten op dit station: ', foreground='blue', font=('Arial', 20), bg='yellow', )
    voorzieningen_txt.pack()
    voorzieningen_txt.place(x=450, y=500)


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
    
    print(ov_fiets, lift, wc, laaden_lossen) 






root.mainloop()























