a = int(input('inserisci un numero diverso da 5: '))

while a%5 != 0:
    a = int(input('inserisci un numero: '))
    if a%5 == 0:
        print(a/5)