import datetime
import random


# De lijst met de 3 steden die ik heb gekozen en een random functie om 1 willekeurig station uit de lijst te pakken
stations = ['Amsterdam', 'Utrecht', 'Leiden']
random_station = random.choice(stations)


def opinie():
    naam = str(input('Voer hier uw naam in: '))
    #hoe / te vinden?
    if naam == ('') or naam == (' '):
        print('U heeft er voor gekozen om uw bericht anoniem in te dienen.')
        bericht = input('u kan hier uw bericht anoniem indienen, (de bericht mag uit maximaal 140 karakters bestaan en geen: /): ')

        if len(bericht) > 140: #or bericht.find('/') or naam.find('/'):
            print('U heeft te veel karakters gebruikt of een / gebruikt, probeer het opnieuw')
        else:
            naam = 'anoniem'
            return naam, bericht
            
    else:
        print('Goedendag,', naam, 'U voert uw bericht in onder uw eigen naam.')
        bericht = input('U kan hier uw bericht openbaar indienen, (de bericht mag uit maximaal 140 karakters bestaan): ')
        if len(bericht) > 140 or len(naam) > 200:# or bericht == '/' or naam == '/' 
            print('U heeft te veel karakters gebruikt of een / gebruikt, probeer het opnieuw')
        else:
            return naam, bericht

naam, bericht = opinie()
datum_millisecond = datetime.datetime.now()
datum = datum_millisecond.replace(microsecond=0)


#stuur naar sql
print(naam)
print(bericht)
print(datum)
print(random_station)

#vraag voor docent hoe fliter ik op /




            