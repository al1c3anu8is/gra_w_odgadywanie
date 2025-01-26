def powitanie_i_parametry():
    """Powitanie gracza i ustawienie trybu gry oraz liczby cyfr w kodzie"""
    print("Witaj w grze w odgadywanie!")
    tryb_gry = int(input("Wybierz tryb gry (1: dwóch graczy, 2: gra z komputerem): "))
    dlugosc_kodu = int(input("Podaj liczbę cyfr w kodzie: "))
    return tryb_gry, dlugosc_kodu