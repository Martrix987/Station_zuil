import psycopg2.extras
import psycopg2
import datetime

#er wordt connectie gemaakt met de database
connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 

#De query wordt uitgevoerd en je krijg het een bericht terug die je moet goedkeuren of afkeuren
query = """SELECT     bericht
           FROM       bericht      g, 
                      moderatie    m
           where      (goedkeuring = 0 or goedkeuring is NULL) 
           limit      1   
           ;"""

#connectie wordt gesloten en het bericht wordt opgeslagen in de variable 'bericht'
cursor.execute(query)
berichten = cursor.fetchmany()
conn.close()

#bericht wordt een string en aan de mod laten zien
print('\n')
for bericht in berichten:
    con_bericht = (bericht[0])
print(con_bericht)
'''
moet moet hier bepalen of het bericht netjes is en hij moet zijn ID invullen (zodat wij weten welke mod het heeft beoordeeld)
 0 wordt als niet gekeurd gezien (default waarde uit DB = 0)
 1 = goegekeurd
 2 = afgekeurd
indien notatie incorrect (goedkeuring wordt 0 en word dus weer opneiw gevraagd) 
'''
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

#informatie voor de gebruiker
print('\nDe volgende informatie is succesvol opgeslagen: ')
print('Moderator ID: ', mod_id)
print('Keuring: ', keuring)
print('De datum en de tijd: ',datum_tijd, '\n')

#wordt connectie gemaakt met de DB
connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#de informatie word in de DB gezet (kijk logisch datamodel)
cursor.execute("update bericht set datumtijd_beoordeling = %s, goedkeuring = %s, mod_id = %s WHERE bericht = %s", (datum_tijd, keuring, mod_id, con_bericht))

#commit en einde connectie
conn.commit()
cursor.close()
conn.close()