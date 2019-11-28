import random
try:
    ileliczb = int(input("Ilość liczb do odgadnięcia: "))
    maksliczba = int(input("Maksymalna losowana liczba "))
    if maksliczba < ileliczb:
        print("Błędne dane!")
        exit()
except ValueError:
    print("Błędne dane!")
    exit()
lista = []
i = 0
while i < ileliczb:
    liczba = random.randint(1, maksliczba)
    if lista.count(liczba) == 0:
        lista.append(liczba)
        i += 1
for i in range(3):
    print("Wytypuj {} z {} liczb".format(ileliczb, maksliczba))
    typy = set()
    i = 0
    while i < ileliczb:
        try:
            typ = int(input("Podaj liczbę {}: ".format(i+1)))
        except ValueError:
            print("Błędne dane!")
            continue
        if 0 < typ <= maksliczba and typ not in typy:
            typy.add(typ)
            i += 1
    trafione = set(lista) & typy
    if trafione:
        print("\nIlość trafień: {}".format(len(trafione)))
        print("Trafione liczby: ", trafione)
    else:
        print("Brak trafień. Spróbuj jeszcze raz!")
    print("\n" + "x" * 40 + "\n")
print("Wylosowane liczby ", lista)