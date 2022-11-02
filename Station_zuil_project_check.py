
import psycopg2.extras
import psycopg2
import datetime


print('\n')
connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
query = """SELECT     bericht
           FROM       gebruikers_invoer   g, 
                      moderatie           m
           where      g.bericht_id = m.bericht_id
           and      (  goedkeuring = 0 or goedkeuring is NULL )
           ;"""
cursor.execute(query)
print(cursor.fetchall())
conn.close()







test_keuring = int(input('\nControleer of de tekst hierboven fatsoenlijk is, indien de tekst fatsoenlijk is type 1 maar als de tekst niet fatsoenlijk is typ 2 \n: '))
naam_moderator = input('Voer hier de naam van de moderator in: ')
email_moderator = input('Voer hier het email van de moderator in: ')
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

cursor.execute("INSERT INTO moderatie (datumtijd_beoordeling, naam, bericht, station) VALUES (%s, %s, %s, %s)", (datum_tijd, keuring, naam_moderator, email_moderator))

conn.commit()
cursor.close()
conn.close()











