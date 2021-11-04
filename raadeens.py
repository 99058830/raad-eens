import random

print('''Welkom
Je kunt hier punten verzamelen ₳, doe je mee?
''')
punten = 0
for i in range(20):
    if i != 0 and i != 19:
        gokkenInput = input('Wil je opnieuw gokken? stoppen = nee >>> ').lower()
        if gokkenInput == 'nee':
            print('Fijne dag verder!')
            print('je punten waren: ₳' + str(punten))
            exit()
    randomGetal = random.randint(1,1000)
    for x in range(1000):
        raden = int(input('Wat denk je dat het getal is? >>> '))
        if raden == randomGetal:
            print('Het getal is juist, je krijg een point erbij')
            punten += 1
            break
        if abs(raden - randomGetal) <= 20:
            print('Je bent heel warm')
        elif abs(raden - randomGetal) <= 50:
            print('Je bent warm')
        if raden > randomGetal:
            print('Lager ↓')
        if raden < randomGetal:
            print('Hoger ↑')
    print('₳' + str(punten))