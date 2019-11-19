# -*- coding: utf-8 -*-
#sktypt do obliczania stanu konta na lokacie
print("Program do obliczania lokalty")
stan_wej = float(input("Podaj stan początkowy konta w zł: "))
stopa = float(input("Podaj stopę oprocentowania rocznego w %: "))
stopa = stopa / 100
lata = int(input("Podaj liczbę lat na lokacie: "))
stopam = stopa / 12 
print("Twoja miesięczna stopa oprocentowania wynosi: {:.4f}".format(stopam))
result = stan_wej * (1 + stopam)**(12*lata)
print("Twój stan początkowy wynoszący {}zł, przez okres {} lat na lokacie rocznej \
{:.1f}% urośnie do {:.2f}zł.".format(stan_wej, lata, stopa*100, result))
