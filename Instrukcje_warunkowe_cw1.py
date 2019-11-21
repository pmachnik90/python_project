# Zadanie 1
age = int(input("Podaj swój wiek: "))
if age > 100:
    print ("200 lat!")
elif age < 18:
    print ("Użytkownik niepełnoletni, do pełnoletności pozostało: {}".format(18-age))
else:
    print ("Użytkownik pełnoletni")

