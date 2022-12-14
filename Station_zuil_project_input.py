import psycopg2
import psycopg2.extras
import datetime
import random


# De lijst met de 3 steden die ik heb gekozen en een random functie om 1 willekeurig station uit de lijst te pakken
stations = ['Amsterdam', 'Utrecht', 'Leiden']
random_station = random.choice(stations)

#Een functie waarin een bepaald aantal regels worden gecontroleerd zoals de lengte van de naam en de lengte van het bericht.
#Ook wordt er gecontroleerd of de gebruiker een naam heeft ingevoerd, indein niet gebeurd wordt de naam anoniem
def opinie():
    naam = str(input('Voer hier uw naam in: '))
    if naam == ('') or naam == (' '):
        print('U heeft er voor gekozen om uw bericht anoniem in te dienen.')
        bericht = input('u kan hier uw bericht anoniem indienen, (de bericht mag uit maximaal 140 karakters bestaan en geen: /): ')

#Hier wordt een foutmelding gegeven als het bericht te lang is en de naam wordt doorgegeven als anoniem
        if len(bericht) > 140 or len(naam) > 45:
            print('U heeft te veel karakters gebruikt voor uw naam of uw bericht, probeer het opnieuw')
        else:
            naam = 'anoniem'
            return naam, bericht

#Hier wordt ook weer een foumelding gegeven indien het bericht of de naam te lang is(alleen dit is voor als iemand een eigen naam invult)            
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


#Dit wordt gestuurd naar de database
print('\nDe volgende informatie is succesvol opgeslagen: ')
print('Naam: ', naam)
print('Bericht: ', bericht)
print('De datum en de tijd: ',datum)
print('Uw huidige locatie: ',random_station, '\n')


#Hier wordt de connectie gemaakt met de database met de bijbehorden identiale
connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#Hier wordt de datum, naam, bericht en een random station (keuzen uit: Leiden, Utrecht en Amsterdam) in de database toegevoegd
cursor.execute("INSERT INTO bericht (datumtijd_bericht, naam, bericht, station) VALUES (%s, %s, %s, %s)", (datum, naam, bericht, random_station))

#Database wordt commit en connectie wordt gesloten
conn.commit()
cursor.close()
conn.close()