import psycopg2.extras
import psycopg2
import datetime


print('\n')
connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
query = """SELECT     bericht
           FROM       bericht      g, 
                      moderatie    m
           where      (goedkeuring = 0 or goedkeuring is NULL) 
           limit      1   
           ;"""
cursor.execute(query)
bericht = cursor.fetchall()
conn.close()


print(bericht)


test_keuring = int(input('\nControleer of de tekst hierboven fatsoenlijk is, indien de tekst fatsoenlijk is type 1 maar als de tekst niet fatsoenlijk is typ 2 \n: '))
mod_id = int(input('\nVoer hier uw modderator ID in: '))
datum_tijd = datetime.datetime.now()
if test_keuring == 1:
    print('Oke het bericht wordt nu goed gekeurd.')
    keuring = 1
elif test_keuring == 2:
    print('Het bericht is nu afgekeurd.')
    keuring = 2
else:
    print('De notatie was niet goed en de keuring zal niet worden doorgevoerd.')
    keuring = 0


connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute("update bericht set datumtijd_beoordeling = '2022-11-02 010:35:23', goedkeuring = 1, mod_id = 1 WHERE bericht = 'hello world1'")
#cursor.execute("update INTO bericht (datumtijd_beoordeling, goedkeuring, mod_id, station) VALUES (%s, %s, %s)", (datum_tijd, keuring, mod_id))

conn.commit()
cursor.close()
conn.close()











