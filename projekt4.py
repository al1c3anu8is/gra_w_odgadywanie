import random
def powitanie_i_parametry():
    print("Witaj w grze w odgadywanie!")
    tryb_gry = int(input("Wybierz tryb gry (1: dwóch graczy, 2: gra z komputerem): "))
    dlugosc_szyfru = int(input("Podaj liczbę cyfr w szyfrie: "))
    return tryb_gry, dlugosc_szyfru

def tworzenie_kodu(dlugosc_szyfru):
    return [random.randint(0, 9) for _ in range(dlugosc_szyfru)]
    
def wprowadz_zgadywanie(dlugosc_szyfru):
    while True:
        strona_zgadywania = input(f"Wprowadź swój szyfr ({dlugosc_szyfru} cyfrowy): ")
        if len(strona_zgadywania) == dlugosc_szyfru and strona_zgadywania.isdigit():
            return [int(cyfra) for cyfra in strona_zgadywania]
        print(f"Proszę wprowadzić dokładnie {dlugosc_szyfru} cyfr.")

def ocena_zgadywania(kod, zgadywanie):
      """
    Funkcja sprawdza, ile cyfr w podanym przez gracza szyfrie znajduje się na właściwych miejscach,
    oraz ile cyfr jest obecnych w szyfriie, ale na niewłaściwych miejscach.

    Parametry:
    kod (list[int]): Lista cyfr, które stanowią prawdziwy kod do odgadnięcia.
    strona_zgadywania (list[int]): Lista cyfr próby zgadywania gracza.

    Zwraca:
    tuple:
        - miejsca_poprawne (int): Liczba cyfr, które gracz zgadł na właściwych miejscach.
        - cyfry_poprawne (int): Liczba cyfr, które gracz zgadł, ale są na niewłaściwych miejscach.

    Przykład użycia funkcji:
    >>> ocena_zgadywania([1, 2, 3, 4], [1, 5, 3, 4])
    (2, 2)

    Wyjaśnienie otrzymanego wyniku:
    - miejsca_poprawne: 2 (pierwsza i czwarta cyfra: 1 i 4)
    - cyfry_poprawne: 2 (trzecia cyfra 3 oraz druga cyfra 5 znajdują się w kodzie, ale na innych miejscach w szyfrze)
    """
    miejsca_poprawne = sum(1 for i in range(len(kod)) if kod[i] == zgadywanie[i])
    cyfry_poprawne = sum(min(kod.count(cyfra), zgadywanie.count(cyfra)) for cyfra in set(zgadywanie)) - miejsca_poprawne
    return miejsca_poprawne, cyfry_poprawne

def tryb_dla_graczy(dlugosc_szyfru):
    print(f"Gracz pierwszy: Wprowadź kod ({dlugosc_szyfru} cyfrowy, zapisz go lub zapamiętaj): ", end="")
    kod = [int(cyfra) for cyfra in input().strip()]
    return kod

def tryb_komputerowy(dlugosc_szyfru):
    print("Kod wygenerowany przez komputer.")
    return tworzenie_kodu(dlugosc_szyfru)
def przebieg_gry(tryb_gry, dlugosc_szyfru):
    if tryb_gry == 1:
        kod = tryb_dla_graczy(dlugosc_szyfru)
    else:
        kod = tryb_komputerowy(dlugosc_szyfru)

    liczba_prob = 0  

    while True:
        zgadywanie = wprowadz_zgadywania(dlugosc_szyfru)  
        liczba_prob += 1 
        miejsca_poprawne, cyfry_poprawne = ocena_zgadywanie(kod, zgadywanie)

    
        print(f"Cyfry na właściwych miejscach: {miejsca_poprawne}")
        print(f"Cyfry w kodzie, ale nie na swoich miejscach: {cyfry_poprawne}")

    
        if miejsca_poprawne == dlugosc_szyfru:
            print(f"Gratulacje! Odgadłeś kod w {liczba_prob} próbach.")
            break

def main():
    tryb_gry, dlugosc_szyfru = powitanie_i_parametry() 
    przebieg_gry(tryb_gry, dlugosc_szyfru) 

if __name__ == "__main__":
    main() 
