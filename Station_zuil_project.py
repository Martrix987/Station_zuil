import datetime
from textwrap import fill
def klacht():
    while Invullen is True:
        naam = input('Voer hier uw naam in: ')

        #verander het woord klacht want het mag ook postief
        if naam == (''):
            print('U heeft er voor gekozen om uw klacht anoniem in te dienen.')
            klacht = input('U kan hier uw klacht anoniem indienen, (de klacht mag uit maximaal 140 karakters bestaan): ')
            if len(klacht) < 140:
                print('U heeft te veel karakters gebruikt, probeer het opnieuw')
                return Invullen is True
            else:
                return Invullen is False
        else:
            print('Goedendag,', naam, 'U voert uw klacht in onder uw eigen naam.')
            klacht = input('U kan hier uw klacht openbaar indienen, (de klacht mag uit maximaal 140 karakters bestaan): ')
            if len(klacht) < 140:
                print('U heeft te veel karakters gebruikt, probeer het opnieuw')
                return Invullen is True
            else:
                return Invullen is False
            