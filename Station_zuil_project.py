import datetime


def klacht():
    naam = input('Voer hier uw naam in: ')
    #verander het woord klacht want het mag ook postief --> opinie
    if naam == (''):
        print('U heeft er voor gekozen om uw opinie anoniem in te dienen.')
        opinie = input('U kan hier uw opinie anoniem indienen, (de opinie mag uit maximaal 140 karakters bestaan): ')
        if len(opinie) < 140:
            print('U heeft te veel karakters gebruikt, probeer het opnieuw')
            break
        else:
            return naam, opinie
            
    else:
        print('Goedendag,', naam, 'U voert uw opinie in onder uw eigen naam.')
        opinie = input('U kan hier uw opinie openbaar indienen, (de opinie mag uit maximaal 140 karakters bestaan): ')
        if len(opinie) < 140:
            print('U heeft te veel karakters gebruikt, probeer het opnieuw')
            break
        else:
            return naam, opinie

klacht()








            