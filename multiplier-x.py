nummer = int(input('van welk getal wilt u de tafel zien: '))

def tafels(nummer:int):
    for i in range(1,11):
        print(str(i) + 'x' + str(nummer) + '= ' + str(i*nummer))

tafels(nummer)


