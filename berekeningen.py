def myFunction():
    calc = input('wat voor berekening wilt u doen + - / x +1 of -1: ')
    if calc == '+':
        number1 = int(input('kies een getal '))
        number2 = int(input('kies een getal '))
        print('{}'.format(number1) + '+' + '{}'.format(number2) + '=' + str(number1 + number2))
    elif calc == '-':
        number1 = int(input('kies een getal '))
        number2 = int(input('kies een getal '))
        print('{}'.format(number1) + '-' + '{}'.format(number2) + ' = ' + str(number1 - number2))
    elif calc == '/':
        number1 = int(input('kies een getal '))
        number2 = int(input('kies een getal '))
        print('{}'.format(number1) + '-' + '{}'.format(number2) + ' = ' + str(number1 / number2))
    elif calc == 'x':
        number1 = int(input('kies een getal '))
        number2 = int(input('kies een getal '))
        print('{}'.format(number1) + 'x' + '{}'.format(number2) + ' = ' + str(number1 * number2))
    elif calc == '+1':
        number1 = int(input('kies een getal '))
        print('{}'.format(number1) + '+' + '1' + ' = ' + str(number1 + 1))
    elif calc == '-1':
        number1 = int(input('kies een getal '))
        print('{}'.format(number1) + '-' + '1' + ' = ' + str(number1 - 1))

myFunction()