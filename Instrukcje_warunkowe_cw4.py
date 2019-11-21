# Imiona
names_w = ["Ania", "Katarzyna", "Natalia", "Adrianna", "Paulina"]
names_m = ["Piotr", "Łukasz", "Tomasz","Adrian", "Damian", "Dariusz"]
name = str(input("Podaj swoje imie: "))
name = name.capitalize()
print (name)
if name in names_w:
    print("Twoje imie jest żeńskie")
elif name in names_m:
    print("Twoje imie jest męskie")
else:
    print("Nie znam takiego imienia.")
    dec = str(input("Czy zapisać Twoje imię do bazy? [T/N]: "))
    dec = dec.upper()
    if dec == "N":
        print("Imie nie zostało zapisane.")
    else:
        dec2 = str(input("Czy Twoje imie jest męskie czy żeńskie? [K/M]: "))
        dec2 = dec2.upper()
        if dec2 == "K":
            names_w.append(name)
            print("Zapisano w kartotece imion żeńskich {}".format(names_w))
        elif dec2 == "M":
            names_m.append(name)
            print("Zapisano w kartotece imion męskich {}".format(names_m))
        else:
            print("Podano złą wartość")

    
    
