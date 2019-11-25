# Wprowadzanie dowolnej liczby imion
names = str(input("Podaj imiona oddzielone spacją: ") + " ")
name = ""
lists = []
for i in names:
    if i == " ":
        lists.append(name)
        name = ""
    else:
        name += i
for o in lists:
    print("Witaj {}".format(o))


imiona=input("podaj imiona oddzielone spacją: ")
for g in imiona.split():
       print("Cześć "+g)

