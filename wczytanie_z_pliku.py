def wczytaj_dane_z_pliku(nazwa_pliku="m10n200.txt"):
    lista_danych = []
    try:
        with open(nazwa_pliku, 'r') as plik:
            for linia in plik:
                liczba = int(linia.strip())
                lista_danych.append(liczba)
    except FileNotFoundError:
        print(f"BLAD: Plik o nazwie '{nazwa_pliku}' nie zostal znaleziony.")
    except ValueError:
        print(f"BLAD: W pliku '{nazwa_pliku}' znajduje się linia, ktorej nie mozna zamienic na liczbe.")
    
    return lista_danych