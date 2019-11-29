#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from extra_lotek import ustawienia, losujliczby, pobierztypy, wyniki
from extra_lotek import czytaj_ust, zapisz_ust, czytaj_str, zapisz_str
import time


def main(args):
    #ustawienia gry
    nick, ileliczb, maksliczba, ilelos = ustawienia()

    #Losujemy liczby
    lista = losujliczby(ileliczb,maksliczba)

    #pobieramy typy użytkownika i sprawdzamy, ile liczb trafił
    for i in range(ilelos):
        typy = pobierztypy(ileliczb, maksliczba)
        iletraf = wyniki(set(lista), typy)

    nazwapliku2 = nick + ".txt" # nazwa pliku z historią losowań do pliku txt
    losowania = czytaj_str(nazwapliku2)

    losowania.append({
        "czas": time.time(),
        "dane": (ileliczb, maksliczba),
        "wylosowane": lista,
        "trafienia": iletraf
    })
    zapisz_str(nazwapliku2, losowania)

    print("Wylosowane liczby ", lista)
    return  0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
