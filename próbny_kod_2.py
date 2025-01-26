def main():
    """main - funkcja, która będzie uruchomiała całą grę w odgadywanie"""
    tryb_gry, dlugosc_szyfru = powitanie_i_parametry()  # ustawienie przez gracza trybu gry oraz długości szyfru
    przebieg_gry(tryb_gry, dlugosc_szyfru)  # rozpoczęcie gry

if __name__ == "__main__":
    main()  # ostateczne uruchamianie gry w odgadywanie