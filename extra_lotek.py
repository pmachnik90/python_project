#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import os
import json

def ustawienia():
    #Funkcja pobiera nick użytkownika, ilość losowanych liczb, maksymalną losowaną wartość
    #oraz ilość prób. Pozwala określić stopień trudności gry.

    nick = input("Podaj nick: ")
    nazwapliku = nick + ".ini"
    gracz = czytaj_ust(nazwapliku)
    odp = None
    if gracz:
        print("Twoje ustawienia:\nLiczb: %s\nZ Maks: %s\nLosowań: %s" %
              (gracz[1], gracz[2], gracz[3]))
        odp = input("Zmieniasz (t/n)? ")

    if not gracz or odp.lower() == "t":
        while True:
            try:
                ileliczb = int(input("Ilość liczb do odgadnięcia: "))
                maksliczba = int(input("Maksymalna losowana liczba "))
                if maksliczba < ileliczb:
                    print("Błędne dane!")
                    continue
                ilelos = int(input("Ile losowań: "))
                break
            except ValueError:
                print("Błędne dane!")
                continue
        gracz = [nick, str(ileliczb), str(maksliczba), str(ilelos)]
        zapisz_ust(nazwapliku, gracz)
    return gracz[0:1] + [int(x) for x in gracz[1:4]]

def losujliczby(ileliczb, maksliczba):
    """Funkcja losuje ile unikalnych liczb całkowitych od 1 do maks """
    lista = []
    i = 0
    while i < ileliczb:
        liczba = random.randint(1, maksliczba)
        if lista.count(liczba) == 0:
            lista.append(liczba)
            i += 1
    return lista

def pobierztypy(ileliczb, maksliczba):
    """Funkcja pobiera od użytkownika jego typy wylosowanych liczb"""
    print("Wytypuj {} z {} liczb".format(ileliczb, maksliczba))
    typy = set()
    i = 0
    while i < ileliczb:
        try:
            typ = int(input("Podaj liczbę {}: ".format(i+1)))
        except ValueError:
            print("Błędne dane!")
            continue
        if 0 < typ <= maksliczba and typ not in typy:
            typy.add(typ)
            i += 1
    return typy

def wyniki(lista, typy):
    """Funkcja porównuje wylosowane i wytypowane liczby,
    zwraca ilość trafień"""
    trafione = set(lista) & typy
    if trafione:
        print("\nIlość trafień: {}".format(len(trafione)))
        trafione = ", ".join(map(str, trafione))
        print("Trafione liczby: ", trafione)
    else:
        print("Brak trafień. Spróbuj jeszcze raz!")

    print("\n" + "x" * 40 + "\n")
    return len(trafione)
def czytaj_ust(nazwapliku):
    """Funkcja odczytuje parametry użytkownika z pliku ini"""
    if os.path.isfile(nazwapliku):
        plik = open(nazwapliku, "r")
        linia = plik.readline()
        plik.close()
        if linia:
            return linia.split(";")
    return False

def zapisz_ust(nazwapliku, gracz):
    """Funkcja zapisuje parametry użytkownika do pliku ini"""
    plik = open(nazwapliku, "w")
    plik.write(";".join(gracz))
    plik.close()

def czytaj_json(nazwapliku2):
    """Funkcja odczytuje dane w formacie json z pliku"""
    dane = []
    if os.path.isfile(nazwapliku2):
        with open(nazwapliku2, "r") as plik:
            dane = json.load(plik)
    return dane

def zapisz_json(nazwapliku2, dane):
    """Funkcja zapisuje dane w formacie json do pliku"""
    with open(nazwapliku2, "w") as plik:
        json.dump(dane, plik)

def czytaj_str(nazwapliku2):
    """Funkcja odczytuje dane w formacie txt do pliku"""
    dane = []
    if os.path.isfile(nazwapliku2):
        with open(nazwapliku2, "r") as plik:
            temp = plik.readlines()
            print(temp)
            Slownik2 = {}
            for i in temp:
                Slownik2 = dict((x.strip(), y.strip()) for x, y in (element.split(':') for element in i.split(';')))
                dane.append(Slownik2)
            plik.close()
    return dane

def zapisz_str(nazwapliku2, dane):
    """Funkcja zapisuje dane w formacie txt do pliku"""
    with open(nazwapliku2, "w") as plik:
        for slownik in dane:
            linia = [k + ":" + str(w) for k, w in slownik.items()]
            linia = ";".join(linia)
            plik.write(linia+"\n")
    print("Zapisano")
