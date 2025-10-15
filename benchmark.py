import random

def generuj_dane_automatycznie(max_procesorow=8, max_procesow=30, max_czas_zadania=100, nazwa_pliku="dane.txt"):
    liczba_procesorow = random.randint(2, max_procesorow)
    liczba_procesow = random.randint(liczba_procesorow + 1, max_procesow)
    czasy_wykonania = [random.randint(1, max_czas_zadania) for _ in range(liczba_procesow)]
    
    wynikowa_lista = [liczba_procesorow, liczba_procesow] + czasy_wykonania
    
    try:
        with open('dane.txt', 'w') as plik:
            dane_jako_stringi = [str(liczba) for liczba in wynikowa_lista]
            plik.write("\n".join(dane_jako_stringi))
    except IOError as e:
        print(f"Wystapil blad podczas zapisu do pliku: {e}")

    return wynikowa_lista