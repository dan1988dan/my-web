# THIS PROGRAM IS MADE BY DAN. THIS IS MY FIRST PROJECT IN PYTHON 3.

import sys, random, datetime, os
now = datetime.datetime.now()
time = now.ctime()

def PASSWORD () :                                               # WPROWADZ HASŁO
    HASLO = input ('\nWPROWADŹ HASŁO : ')
    if HASLO != 'Daniel' :
        print ('wprowadzono niepoprawne hasło')
        PASSWORD ()
    while HASLO == 'Daniel' :
        print ('Witaj ' + HASLO)
        break

def MENU () :                                                   # MENU GŁÓWNE
    os.system('cls')
    print (""" 
    ----------------------
    |    MENU GŁÓWNE :     |
    |                      |
    | (1) Formularz        |
    | (2) Ile masz lat     |
    | (3) Kalkulator       |
    | (4) Znajdź liczbę    |
    | (5) Converter        |
    | (9) About            |
    | (0) EXIT             |
     ---------------------- """)
    print ('\n' + time)
    WYBOR = input ()
    if WYBOR == '1' :
        '\n' + FORMULARZ()
    if WYBOR == '2' :
        '\n' + ILELAT ()
    if WYBOR == '0' :
        return sys.exit()
    if WYBOR == '3' :
        '\n' + KALKULATOR()
    if WYBOR == '4' :
        '\n' + ZNAJDZLICZBE()
    if WYBOR == '5' :
        'n' + CONVERTER()
    if WYBOR == '9' :
        '\n\n' + ABOUT()
    else :
        MENU()

def JEDENZERO ():                                               # WYBÓR
    print (' ----------------------')
    print ('| (1) POWTÓRZ          |')
    print ('| (0) EXIT             |')
    print (' ----------------------')

def FORMULARZ () :                                              #FORMULARZ
    os.system('cls')
    print()
    IMIE = input ('Podaj Twoje imię:  ')
    NAZWISKO = input ('Podaj Twoje nazwisko:  ')
    print ('Witaj ' + IMIE + ' ' + NAZWISKO )
    print ()
    JEDENZERO()
    jedenzero = input ()
    if jedenzero == '1' :
        FORMULARZ()
    elif jedenzero == '0' :
        MENU()
    else:
        JEDENZERO()
    print ()

def ILELAT () :                                                 # ILE MASZ LAT
    os.system('cls')
    now = datetime.datetime.now()
    try:
        rokurodzenia = input('Podaj Twój rok urodzenia:  ')
        print('Masz ' + str(int(now.year) - int(rokurodzenia)) + ' lat')
    except:
        ILELAT()
    JEDENZERO()
    jedenzero = input ()
    if jedenzero == '1' :
        ILELAT()
    elif jedenzero == '0' :
        MENU()
    print ()

def KALKULATOR () :                                             # KALKULATOR
    os.system('cls')
    print(' ----------------------')
    print('|    KALKULATOR  :     |')
    print('|                      |')
    print('| (1) Dodawanie        |')
    print('| (2) Odejmowanie      |')
    print('| (3) Mnożenie         |')
    print('| (4) Dzielenie        |')
    print('|                      |')
    print('| (0) EXIT             |')
    print(' ----------------------')
    def DODAWANIE():
        try:
            a = input('a=  ')
            b = input('b=  ')
            print('------')
            print(int(a) + int(b))
            print('------\n\n')
            DODAWANIE()
        except:
            KALKULATOR()
    def ODEJMOWANIE():
        try:
            a = input('a=  ')
            b = input('b=  ')
            print('------')
            print(int(a) - int(b))
            print('------\n\n')
            ODEJMOWANIE()
        except:
            KALKULATOR()
    def MNOŻENIE():
        try:
            a = input('a=  ')
            b = input('b=  ')
            print('------')
            print(int(a) * int(b))
            print('------\n\n')
            MNOŻENIE()
        except:
            KALKULATOR()
    def DZIELENIE():
        try:
            a = input('a=  ')
            b = input('b=  ')
            print('------')
            print(int(a) / int(b))
            print('------\n\n')
            DZIELENIE()
        except:
            KALKULATOR()
    menuKalk = input()
    if menuKalk == '1':
        DODAWANIE()
    elif menuKalk == '2':
        ODEJMOWANIE()
    elif menuKalk == '3':
        MNOŻENIE()
    elif menuKalk == '4':
        DZIELENIE()
    elif menuKalk == '0':
        MENU()
    else:
        KALKULATOR()

def ABOUT () :                                                  # INFORMACJE O AUTORZE
    os.system('cls')
    print ('This program is made by Dan Daniel Olszyk ')
    print ('Contact: danielolszyk1988@gmail.com')
    print ('ENJOY !!!!\n\n')
    print('(0) EXIT)')
    exit = input()
    if exit == '0':
        MENU()

def ZNAJDZLICZBE ():                                            # ZNAJDZ LICZBĘ
    os.system('cls')
    print('Znajdź liczbę od 1 do 5000')
    print ('Masz 10 prób : ')
    losowaliczba = random.randint(1, 5000)
    for x in range(0, 10):
        try:
            liczba = int(input())
            if liczba < losowaliczba:
                print('Za mało\n')
            elif liczba > losowaliczba:
                print('Za dużo\n')
            else:
                break
        except:
            print('Tylko liczby\n')
    try:
        if liczba == losowaliczba:
            print('Bardzo Dobrze')
        else :
            print('Liczba, którą próbowałeś zgadnąć to ' + str(losowaliczba))
    except:
        print ()
    JEDENZERO()
    jedenzero = input()
    if jedenzero == '1':
        ZNAJDZLICZBE()
    elif jedenzero == '0':
        MENU()
    else:
        JEDENZERO()

def CONVERTER () :
    os.system('cls')
    print(' ----------------------')
    print('|     CONVERTER  :     |')
    print('|                      |')
    print('| (1) C  to  F         |')
    print('| (2) F  to  C         |')
    print('| (3) C  to  K         |')
    print('| (4) K  to  C         |')
    print('|                      |')
    print('| (0) EXIT             |')
    print(' ----------------------')
    def celsjuszfarenheit () :
        try:
            celsjusz = input ('Celsjusz :  ')
            fahrenheit = int(celsjusz) * (9/5) + 32
            print ('Fahrenheit :  ' + str(fahrenheit) + '\n')
            celsjuszfarenheit()
        except:
            CONVERTER()
    def fahrenheitcelsjusz () :
        try:
            fahrenheit = input ('Fahrenheit :  ')
            celsjusz =  (int(fahrenheit) - 32) * 5 / 9
            print ('Celsjusz :  ' + str(celsjusz) + '\n')
            fahrenheitcelsjusz()
        except:
            CONVERTER()
    def celsjuszkelvin () :
        try:
            celsjusz = input ('Celsjusz :  ')
            kelvin = int(celsjusz) + 273.15
            print ('Kelvin :  ' + str(kelvin) + '\n')
            celsjuszkelvin()
        except :
            CONVERTER()
    def kelvincelsjusz () :
        try:
            kelvin = input ('Kelvin :  ')
            celsjusz = int(kelvin) - 273.15
            print ('Celsjusz :  ' + str(celsjusz) + '\n')
            kelvincelsjusz()
        except :
            CONVERTER()

    WYBOR = input()
    if WYBOR == '1':
        celsjuszfarenheit()
    elif WYBOR == '2':
        fahrenheitcelsjusz()
    elif WYBOR == '3':
        celsjuszkelvin()
    elif WYBOR == '4':
        kelvincelsjusz()
    elif WYBOR == '0':
        MENU()
    else:
        CONVERTER()

PASSWORD ()
MENU()