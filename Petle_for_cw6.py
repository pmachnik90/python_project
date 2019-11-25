# Tabliczka mnożenia
szer = 35
print("-" * szer)
print("|  Liczba1  |  Liczba2  |  Wynik  |")
print("*" * szer)
for i in range(1,101):
    for j in range(1,11):
        wynik = i*j
        print("|    {:4s}   |    {:4s}   |    {:4s}  |" .format(str(i), str(j), str(wynik)))
print("-" * szer)
