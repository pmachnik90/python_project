# -*- coding: utf-8 -*-
#BMI - dodanie instrukcji warunkowych
print("Oto kalkulator PPM, postępuj zgodnie z instrukcją.")
S = input("Podaj swoją płeć M - mężczyzna, K - kobieta: ")
waga = float(input("Podaj swoją wagę: "))
wzrost = int(input("Podaj swój wzrost w cmentymetrach: "))
wiek = int(input("Podaj swój wiek w latach: "))
wsp1 = 0
wsp2 = 0
if S == "M":
    wsp1 = 5
elif S == "K":
    wsp1 = (-161)
print("Podaj swoją aktywność fizyczną zgodnie z oznaczeniem")
print('''Praca siedząca, brak dodatkowej aktywności fizycznej: 1
Praca niefizyczna, mało aktywny tryb życia: 2
Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu: 3
Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu: 4
Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu: 5''')
AF = int(input("Wpisz oznaczenie: "))
if AF == 1:
    wsp2 = 1.2
elif AF == 2:
    wsp2 = 1.4
elif AF == 3:
    wsp2 = 1.6
elif AF == 4:
    wsp2 = 1.8
elif AF == 5:
    wsp2 = 2.0
else:
    print("Podałeś/aś wartość z poza zakresu")
PPM = 10 * waga + 6.25 * wzrost - 5 * wiek + wsp1
BMI = waga / ((wzrost/100) ** 2)
ocls = ""
if BMI < 18.5:
    ocls = "Niedowaga"
elif 18.5 <= BMI <= 24.0:
    ocls = "Waga normalna"
elif 24.0 < BMI <= 26.5:
    ocls = "Lekka nadwaga"
else:
    ocls = "Nadwaga"
    if 30.0 <= BMI <= 35.0:
        ocls = ocls + ": Otyłość I stopnia"
    elif 35.0 < BMI <= 40.0:
        ocls = ocls + ": Otyłość II stopnia"
    elif BMI > 40:
        ocls = ocls + ": Otyłość III stopnia"
    else:
        ocls
print("Twój współczynnik BMI wynosi:", round(BMI, 3))
print("Twoja klasyfikacja BMI: {}".format(ocls))
print("Twoje dzienne zapotrzebowanie kaloryczne wynosi: %s kcal" % round((PPM * wsp2),3))
