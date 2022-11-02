import psycopg2
import psycopg2.extras
import datetime
import random


# De lijst met de 3 steden die ik heb gekozen en een random functie om 1 willekeurig station uit de lijst te pakken
stations = ['Amsterdam', 'Utrecht', 'Leiden']
random_station = random.choice(stations)


def opinie():
    naam = str(input('Voer hier uw naam in: '))
    if naam == ('') or naam == (' '):
        print('U heeft er voor gekozen om uw bericht anoniem in te dienen.')
        bericht = input('u kan hier uw bericht anoniem indienen, (de bericht mag uit maximaal 140 karakters bestaan en geen: /): ')

# hier wordt een foutmelding gegeven als het bericht of de naam te lang is 
        if len(bericht) > 140 or len(naam) > 45:
            print('U heeft te veel karakters gebruikt voor uw naam of uw bericht, probeer het opnieuw')
        else:
            naam = 'anoniem'
            return naam, bericht
            
    else:
        print('Goedendag,', naam, 'U voert uw bericht in onder uw eigen naam.')
        bericht = input('U kan hier uw bericht openbaar indienen, (de bericht mag uit maximaal 140 karakters bestaan): ')
        if len(bericht) > 140 or len(naam) > 45: 
            print('U heeft te veel karakters gebruikt of een / gebruikt, probeer het opnieuw')
        else:
            return naam, bericht

#de ingevulde en goedgekeurde informatie word uit de defenitie gehaald en in een variable gezet
naam, bericht = opinie()
#de datum en de tijd worden opgevraagd en in de variable datum geplaatst (tijd is tot 4 honderste seconde)
datum = datetime.datetime.now()

keuring = 0

#Dit wordt gestuurd naar de database
print(naam)
print(bericht)
print(datum)
print(random_station)

# Hier wordt de connectie gemaakt met de database met de bijbehorden identiale
connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute("INSERT INTO moderatie (goekeuring) VALUE (%s)", (keuring))
cursor.execute("INSERT INTO gebruikers_invoer (datumtijd_bericht, naam, bericht, station) VALUES (%s, %s, %s, %s)", (datum, naam, bericht, random_station))



conn.commit()
cursor.close()
conn.close()

    






            