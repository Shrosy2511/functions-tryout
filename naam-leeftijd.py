def personal_info():
    print('om het programma te sluiten type stop')
    naam = input('wat is uw naam: ')
    if naam == 'stop':
        exit()
    leeftijd = input('wat is uw leeftijd: ')
    if leeftijd == 'stop':
        exit()
    print('hallo {}'.format(naam) + ' je leeftijd is {}'.format(leeftijd))

while True:
    personal_info()