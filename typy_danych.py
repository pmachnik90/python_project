# spis filmów - słowniki
Serials = {"Sami swoi" : 8, "Nie ma mocnych" : 9, "Kochaj albo rzuć" : 9.5, \
           "Skazany na shawshank" : 9, "Nietykalni" : 7.5}
i = 0
list_f = {}
print("Lista filmów:")
for key in Serials:
    i += 1
    list_f[i] = key
    print("{}. {}".format(i,key))
v_user = int(input("Wybierz numer filmu, który chcesz obejrzeć? "))
if v_user <= i:
    print("Wybrałeś film {}, którego ocena wynosi \
{}".format(list_f[v_user], Serials[list_f[v_user]]))
else:
    v_user2 = input("Podałeś błędą liczbę, czy chcesz dodać nowy film do listy?[T/N] ")
    v_user2 = v_user2.upper()
    if v_user2 == "T":
        v_Skey = input("Podaj nazwę filmu: ")
        v_Svalue = input("Podaj ocenę Twojego filmu: ")
        Serials[v_Skey] = v_Svalue
    elif v_user2 == "N":
        print("Nie chcesz dodać filmu, dziękuję za uwage.")
    else:
        print("Podałeś złą wartość!")
for key,val in Serials.items():
    print(key, "=>", val)
                        
    
