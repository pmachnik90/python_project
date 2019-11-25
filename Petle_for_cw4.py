# Wykonana ilość Użytkownika i sprawdzenie liczby
cnt = int(input("Podaj liczbę wykonań pętli: "))
for i in range(cnt):
    v_cnt = int(input("Podaj liczbę: "))
    if v_cnt%3 == 0 and v_cnt%4 != 0:
        print("Liczba jest podzielna przez 3")
    elif v_cnt%4 == 0 and v_cnt%3 != 0:
        print("Liczba jest podzielna przez 4")
    elif v_cnt%3 == 0 and v_cnt%4 == 0:
        print("Hurra, liczba podzielna przez 3 oraz 4")
    else:
        print("*")

