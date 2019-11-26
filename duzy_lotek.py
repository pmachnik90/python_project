import random
ileliczb = int(input("Ilość liczb do odgadnięcia: "))
maksliczba = int(input("Maksymalna losowana liczba "))
print("Wytypuj {} z {} liczb".format(ileliczb, maksliczba))
lista = []
typy = set()
i = 0
j = 0
while i < ileliczb:
    typ = int(input("Podaj liczbę {}: ".format(i+1)))
    if typ not in typy:
        typy.add(typ)
        i += 1
print("Twoje typy to: ", typy)
while j < ileliczb:
    liczba = random.randint(1,maksliczba)
    if lista.count(liczba) == 0:
        lista.append(liczba)
        j += 1
print("Wylosowane liczby ", lista)
trafione = set(lista) & typy
if trafione:
    print("\nIlość trafień: {}".format(len(trafione)))
    print("Trafione liczby: ", trafione)
else:
    print("Brak trafień. Spróbuj jeszcze raz!")