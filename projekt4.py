import random
def powitanie_i_parametry():
    print("Witaj w grze w odgadywanie!")
    tryb_gry = int(input("Wybierz tryb gry (1: dwóch graczy, 2: gra z komputerem): "))
    dlugosc_szyfru = int(input("Podaj liczbę cyfr w szyfrie: "))
    return tryb_gry, dlugosc_szyfru
    
    """
    Funkcja powitanie_i_parametry() wita użytkownika i pobiera parametry gry.

    Wyświetla także wiadomość powitalną, pyta użytkownika o wybór trybu gry oraz o
    długość szyfru. Zwraca też wybrane parametry.

    Zwracane parametry:
    - int tryb_gry: wartość numeru trybu gry (1: dwóch graczy, 2: gra z komputerem)
    - int dlugosc_szyfru: długość szyfru
    
    Przykład użycia funkcji: 
   < Gracz wybiera 1 tryb > 
   < Gracz wpisuje liczbę 4 >
    tryb_gry, dlugosc_szyfru = powitanie_i_parametry()
    print(f"Wybrany tryb gry: {1}")
    print(f"Długość szyfru: {4})
    
    """

def tworzenie_kodu(dlugosc_szyfru):
    return [random.randint(0, 9) for _ in range(dlugosc_szyfru)]
    
def wprowadz_zgadywanie(dlugosc_szyfru):
    while True:
        strona_zgadywania = input(f"Wprowadź swój szyfr ({dlugosc_szyfru} cyfrowy): ")
        if len(strona_zgadywania) == dlugosc_szyfru and strona_zgadywania.isdigit():
            return [int(cyfra) for cyfra in strona_zgadywania]
        print(f"Proszę wprowadzić dokładnie {dlugosc_szyfru} cyfr.")

def ocena_zgadywanie(kod, zgadywanie):
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
    >>> ocena_zgadywanie([1, 2, 3, 4], [1, 5, 3, 4])
    (2, 2)

    Wyjaśnienie otrzymanego wyniku:
    - miejsca_poprawne: 2 (pierwsza i czwarta cyfra: 1 i 4)
    - cyfry_poprawne: 2 (trzecia cyfra 3 oraz druga cyfra 5 znajdują się w kodzie, ale na innych miejscach w szyfrze)
    """
    if len(kod) != len(zgadywanie):
    raise ValueError("Długości kodu i zgadywania muszą być takie same!")
    miejsca_poprawne = sum(1 for i in range(len(kod)) if kod[i] == zgadywanie[i])
    cyfry_poprawne = sum(min(kod.count(cyfra), zgadywanie.count(cyfra)) for cyfra in set(zgadywanie)) - miejsca_poprawne
    return miejsca_poprawne, cyfry_poprawne

def tryb_dla_graczy(dlugosc_szyfru):
    from getpass import getpass
    print(f"Gracz pierwszy: Wprowadź kod ({dlugosc_szyfru} cyfrowy, zapisz go lub zapamiętaj): ", end="")
    kod = [int(cyfra) for cyfra in getpass("").strip()]
    return kod
    
    """
    Funkcja służy do wprowadzenia kodu przez pierwszego gracza.

    Parametry:
    dlugosc_szyfru (int): Długość kodu, który ma wprowadzić gracz.

    Zwraca:
    list: Lista cyfr, które zostały wprowadzone przez gracza.

    Przykład użycia funkcji: 
    
    dlugosc_szyfru = 4
    kod = tryb_dla_graczy(dlugosc_szyfru)
    print(f"Gracz pierwszy wprowadził kod: {kod}")
    """

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
        zgadywanie = wprowadz_zgadywanie(dlugosc_szyfru)  
        liczba_prob += 1 
        miejsca_poprawne, cyfry_poprawne = ocena_zgadywanie(kod, zgadywanie)

    
        print(f"Cyfry na właściwych miejscach: {miejsca_poprawne}")
        print(f"Cyfry w kodzie, ale nie na swoich miejscach: {cyfry_poprawne}")

    
        if miejsca_poprawne == dlugosc_szyfru:
            print(f"Gratulacje! Szyfr został złamany w {liczba_prob} próbach.")
            break

def main():
    tryb_gry, dlugosc_szyfru = powitanie_i_parametry() 
    przebieg_gry(tryb_gry, dlugosc_szyfru) 

if __name__ == "__main__":
    main() 
