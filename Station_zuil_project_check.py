
import psycopg2.extras
import psycopg2
import datetime



connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) # DictCursor, not the default cursor!
query = """SELECT     bericht
           FROM       gebruikers_invoer   g, 
                      moderatie           m
           where      gi.datumtijd_bericht = m.datumtijd_bericht
           and        goedkeuring = 0
           ;"""



cursor.execute(query)
print(cursor.fetchall())
conn.close()





























keuring = bool(input('\nControleer of de tekst hierboven fatsoenlijk is, indien de tekst fatsoenlijk is schrijf True maar als de tekst niet fatsoenlijk is schrijf False'))
naam_moderator = input('Voer hier de naam van de moderator in: ')
email_moderator = input('Voer hier het email van de moderator in: ')
datum_tijd = datetime.datetime.now()

connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute("INSERT INTO moderatie (datumtijd_beoordeling, naam, bericht, station) VALUES (%s, %s, %s, %s)", (datum_tijd, keuring, naam_moderator, email_moderator))


conn.commit()
cursor.close()
conn.close()











