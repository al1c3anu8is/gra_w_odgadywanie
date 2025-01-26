def powitanie_i_parametry():
    print("Witaj w grze w odgadywanie!")
    tryb_gry = int(input("Wybierz tryb gry (1: dwóch graczy, 2: gra z komputerem): "))
    dlugosc_szyfru = int(input("Podaj liczbę cyfr w szyfrie: "))
    return tryb_gry, dlugosc_szyfru

def tworzenie_kodu(dlugosc_szyfru):
    return [random.randint(0, 9) for _ in range(dlugosc_szyfru)]
    
def wprowadz_zgadywanie(dlugosc_szyfru):
    while True:
        strona_zgadywania = input(f"Wprowadź swój szyfr ({dlugosc_szyfru} cyfr): ")
        if len(strona_zgadywania) == dlugosc_szyfru and strona_zgadywania.isdigit():
            return [int(cyfra) for cyfra in strona_zgadywania]
        print(f"Proszę wprowadzić dokładnie {dlugosc_szyfru} cyfr.")

def ocen_zgadanie(kod, zgadywanie):
    miejsca_poprawne = sum(1 for i in range(len(kod)) if kod[i] == zgadywanie[i])
    cyfry_poprawne = sum(min(kod.count(cyfra), zgadywanie.count(cyfra)) for cyfra in set(zgadywanie)) - miejsca_poprawne
    return miejsca_poprawne, cyfry_poprawne
