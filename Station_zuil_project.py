import datetime
import random



stations = ['Amsterdam', 'Utrecht', 'Leiden']
print(random.choice(stations))


def opinie():
    naam = input('Voer hier uw naam in: ')
    #hoe / te vinden?
    if naam == ('') or naam == (' '):
        print('U heeft er voor gekozen om uw opinie anoniem in te dienen.')
        opinie = input('u kan hier uw opinie anoniem indienen, (de opinie mag uit maximaal 140 karakters bestaan en geen: /): ')
        if len(opinie) > 140 or opinie.find('/') or naam.find('/') or len(naam) > 200:
            print('U heeft te veel karakters gebruikt of een / gebruikt, probeer het opnieuw')
        else:
            return 'anoniem', opinie
            
    else:
        print('Goedendag,', naam, 'U voert uw opinie in onder uw eigen naam.')
        opinie = input('U kan hier uw opinie openbaar indienen, (de opinie mag uit maximaal 140 karakters bestaan): ')
        if len(opinie) > 140 or opinie == '/' or naam == '/' or len(naam) > 200:
            print('U heeft te veel karakters gebruikt of een / gebruikt, probeer het opnieuw')
        else:
            return naam, opinie

naam_bericht = opinie()
datum = 0


#stuur naar sql
print(naam_bericht)
print(datum)
print(stations)

#vraag voor docent hoe fliter ik op /




            