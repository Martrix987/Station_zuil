import psycopg2.extras
import psycopg2
import datetime


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
bericht = cursor.fetchmany()
conn.close()

print('\n')
for berichten in bericht:
    con_bericht = berichten['bericht']
print(con_bericht)



test_keuring = int(input('\nControleer of de tekst hierboven fatsoenlijk is, indien de tekst fatsoenlijk is type 1 maar als de tekst niet fatsoenlijk is typ 2 \n: '))
mod_id = int(input('Voer hier uw modderator nummer (ID) in: '))
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


print(datum_tijd)
print(keuring)
print(mod_id)
print(con_bericht)


connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute("update bericht set datumtijd_beoordeling = %s, goedkeuring = %s, mod_id = %s WHERE bericht = %s", (datum_tijd, keuring, mod_id, con_bericht))

conn.commit()
cursor.close()
conn.close()



