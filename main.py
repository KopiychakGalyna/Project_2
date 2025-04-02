"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Galyna Kopiychak
email: galynakopiychak@outlook.com
"""

import random
import time


# funkce pro výpočet trvání hry
def zformatuj_cas(zacatek: float, konec: float) -> str:
    """Spočítá, jak dlouho trvala hra - vrátí to v minutách a v sekundách."""
    celkem_sekund = int(konec - zacatek)
    minuty = celkem_sekund // 60
    sekundy = celkem_sekund % 60
    return f"{minuty} min {sekundy} sec"


# funkce pro vytvoření tajného čísla
def vytvor_tajne_cislo() -> str:
    """Vygeneruje náhodné 4místné číslo s různými číslicemi, ale nezačíná nulou."""
    cisla = list(range(10))
    random.shuffle(cisla)
    if cisla[0] == 0:
        cisla[0], cisla[1] = cisla[1], cisla[0]
    return ''.join(map(str, cisla[:4]))


# funkce, co ověří, jestli vstup hráče je v pořádku
def kontrola_vstupu(vstup: str) -> bool:
    """Zkontroluje, jestli hráč zadal platné číslo - 4 číslice, každá jiná, nezačíná nulou."""
    return (
        len(vstup) == 4 and 
        vstup.isdigit() and 
        len(set(vstup)) == 4 and 
        vstup[0] != '0'
    )

# funkce, co porovná hádání s tajným číslem
def vyhodnot_tip(tajne_cislo: str, hadani: str) -> tuple[int, int]:
    """Spočítá býky a krávy: býk = správná číslice na správném místě, kráva = jen číslice."""
    byci = sum(1 for t, h in zip(tajne_cislo, hadani) if t == h)
    kravy = sum(1 for h in hadani if h in tajne_cislo) - byci
    return byci, kravy


# funkce, která vrátí výstup správně podle počtu (1 bull / 2 bulls)
def format_vysledek(byci: int, kravy: int) -> str:
    """Vrátí text s počtem bulls a cows - podle toho, kolik jich je (jednotné/množné)."""
    byk = "bull" if byci == 1 else "bulls"
    krava = "cow" if kravy == 1 else "cows"
    return f"{byci} {byk}, {kravy} {krava}"


# hlavní funkce hry
def hra() -> None :
    """Tady začíná a probíhá celá hra - pozdrav, hádání, počítání pokusů i čas."""
    print("""
Hi there!
-----------------------------------------------
I've generated a random 4-digit number for you.
Let's play a bulls and cows game.
Type 'exit' or 'q' to quit anytime.
----------------------------------------------- 
""")

    tajne_cislo = vytvor_tajne_cislo()
    pokusy = 0
    zacatek = time.time()

    while True:
        hadani = input("Enter a number:\n" + "-"*47 + "\n>>> ").strip()
        
        if hadani.lower() in ('exit', 'q'):
            print(f"Game over! The secret number was: {tajne_cislo}")
            break

        if not kontrola_vstupu(hadani):
            print("Invalid input. Please enter a unique 4-digit number not starting with 0.")
            continue

        pokusy += 1
        byci, kravy = vyhodnot_tip(tajne_cislo, hadani)
        print(format_vysledek(byci, kravy) + "\n" + "-"*47)
        

        if byci == 4:
           konec = time.time()
           trvani = zformatuj_cas(zacatek, konec)
           print(f"Correct, you've guessed the right number in {pokusy} guesses!")
           print(f"It took you {trvani}.")
           print("-"*47)
           print("That's amazing!")
           break

# tohle zajistí, že se hra spustí jen když se pustí přímo tenhle soubor
if __name__ == "__main__":
    hra()
    

    

       
