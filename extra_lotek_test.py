#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from extra_lotek import ustawienia, losujliczby, pobierztypy, wyniki
from extra_lotek import czytaj_ust, zapisz_ust, czytaj_json, zapisz_json
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

    nazwapliku = nick + ".json" # nazwa pliku z historią losowań
    losowania = czytaj_json(nazwapliku)

    losowania.append({
        "czas": time.time(),
        "dane": (ileliczb, maksliczba),
        "wylosowane": lista,
        "trafienia": iletraf
    })
    zapisz_json(nazwapliku, losowania)

    print("Wylosowane liczby ", lista)
    return  0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))