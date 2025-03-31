"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Galyna Kopiychak
email: galynakopiychak@outlook.com
"""

import random
import time

# funkce pro výpočet trvání hry
def zformatuj_cas(zacatek, konec):
    celkem_sekund = int(konec - zacatek)
    minuty = celkem_sekund // 60
    sekundy = celkem_sekund % 60
    return f"{minuty} min {sekundy} sec"

#funkce pro vytvoření tajného 4místného čísla s unikátními číslicemi (bez začátku 0)
def vytvor_tajne_cislo():
    cisla = list(range(10))
    random.shuffle(cisla)
    if cisla[0] == 0:
        cisla[0], cisla[1] = cisla[1], cisla[0]
    return ''.join(map(str, cisla[:4]))

# funkce pro ověření správnosti vstupu od hráče
def kontrola_vstupu(vstup):
    return (
        len(vstup) == 4 and 
        vstup.isdigit() and 
        len(set(vstup)) == 4 and 
        vstup[0] != '0'
    )

# funkce pro vyhodnocení tipu – spočítá bulls a cows
def vyhodnot_tip(tajne_cislo, hadani ):
    byci = sum(1 for t, h in zip(tajne_cislo, hadani) if t == h)
    kravy = sum(1 for h in hadani if h in tajne_cislo) - byci
    return byci, kravy

# funkce pro správný výpis slova bull/bulls a cow/cows
def format_vysledek(byci, kravy):
    byk = "bull" if byci == 1 else "bulls"
    krava = "cow" if kravy == 1 else "cows"
    return f"{byci} {byk}, {kravy} {krava}"

# hlavní funkce hry
def hra():
    print("Hi there!\n" + "-"*30)
    print("I've generated a random 4-digit number for you.")
    print("Let's play a bulls and cows game.")
    print("Type 'exit' or 'q' to quit anytime.")
    print("-"*30)

    tajne_cislo = vytvor_tajne_cislo()
    pokusy = 0
    zacatek = time.time()

    while True:
        hadani = input("Enter a number:\n" + "-"*30 + "\n>>> ").strip()
        
        if hadani.lower() in ('exit', 'q'):
            print(f"Game over! The secret number was: {tajne_cislo}")
            break

        if not kontrola_vstupu(hadani):
            print("Invalid input. Please enter a unique 4-digit number not starting with 0.")
            continue

        pokusy += 1
        byci, kravy = vyhodnot_tip(tajne_cislo, hadani)
        print(format_vysledek(byci, kravy) + "\n" + "-"*30)
        

        if byci == 4:
           konec = time.time()
           trvani = zformatuj_cas(zacatek, konec)
           print(f"Correct, you've guessed the right number in {pokusy} guesses!")
           print(f"It took you {trvani}.")
           print("-"*30)
           print("That's amazing!")
           break


hra()
    

    

       
