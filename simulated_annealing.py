import random
import math

def oblicz_cmax(przydzial, czasy, procesory):
    """Oblicza Cmax (makespan) dla danego przydziału zadań."""
    if not czasy:
        return 0
    
    obciazenie_procesorow = [0] * procesory
    for i, czas_zadania in enumerate(czasy):
        # przydzial[i] to numer maszyny (0...procesory-1) dla zadania i
        maszyna = przydzial[i]
        obciazenie_procesorow[maszyna] += czas_zadania
        
    return max(obciazenie_procesorow)

def generuj_rozwiazanie_poczatkowe(czasy, procesory):
    """
    Tworzy rozwiązanie początkowe używając tej samej logiki, co Twój
    oryginalny algorytm (List Scheduling).
    Zwraca listę, gdzie indeks to zadanie, a wartość to maszyna.
    """
    liczba_zadan = len(czasy)
    przydzial = [0] * liczba_zadan  # Lista: przydzial[i] = maszyna dla zadania i
    obciazenie_procesorow = [0] * procesory

    # Implementacja logiki z Twojego pliku przydzial_procesow.py
    # Pierwsze 'procesory' zadań na osobne maszyny
    for i in range(min(procesory, liczba_zadan)):
        przydzial[i] = i
        obciazenie_procesorow[i] = czasy[i]

    # Pozostałe zadania na maszynę z najmniejszym obciążeniem
    for i in range(procesory, liczba_zadan):
        idx_min_obciazenia = obciazenie_procesorow.index(min(obciazenie_procesorow))
        przydzial[i] = idx_min_obciazenia
        obciazenie_procesorow[idx_min_obciazenia] += czasy[i]
        
    return przydzial

def generuj_sasiada(rozwiazanie, procesory):
    """
    Generuje sąsiednie rozwiązanie (sąsiada) poprzez losową zmianę.
    Strategia: Wybierz losowe zadanie i przenieś je na inną, losową maszynę.
    """
    if not rozwiazanie:
        return []

    nowe_rozwiazanie = list(rozwiazanie) # Ważne: stwórz kopię!
    
    # Wybierz losowe zadanie
    idx_zadania = random.randint(0, len(nowe_rozwiazanie) - 1)
    stara_maszyna = nowe_rozwiazanie[idx_zadania]
    
    # Wybierz nową, inną maszynę
    nowa_maszyna = random.randint(0, procesory - 1)
    while nowa_maszyna == stara_maszyna and procesory > 1:
        nowa_maszyna = random.randint(0, procesory - 1)
        
    # Przenieś zadanie
    nowe_rozwiazanie[idx_zadania] = nowa_maszyna
    
    return nowe_rozwiazanie

def symulowane_wyzarzanie(czasy, procesory, T_start, T_stop, alfa, iteracje_na_temp):
    """
    Główna pętla algorytmu Symulowanego Wyżarzania.
    
    :param czasy: Lista czasów wykonania poszczególnych zadań.
    :param procesory: Liczba dostępnych procesorów (maszyn).
    :param T_start: Temperatura początkowa.
    :param T_stop: Temperatura końcowa (kryterium stopu).
    :param alfa: Współczynnik schładzania (np. 0.99).
    :param iteracje_na_temp: Liczba iteracji (prób) na każdym poziomie temperatury.
    :return: (najlepszy_koszt, najlepsze_rozwiazanie)
    """
    
    T = T_start
    
    # Krok 1: Wygeneruj rozwiązanie początkowe
    aktualne_rozwiazanie = generuj_rozwiazanie_poczatkowe(czasy, procesory)
    aktualny_koszt = oblicz_cmax(aktualne_rozwiazanie, czasy, procesory)
    
    # Śledzimy najlepsze dotychczas znalezione rozwiązanie
    najlepsze_rozwiazanie = list(aktualne_rozwiazanie)
    najlepszy_koszt = aktualny_koszt
    
    # Krok 2: Pętla schładzania
    while T > T_stop:
        # Krok 3: Pętla wewnętrzna (iteracje dla danej temperatury)
        for _ in range(iteracje_na_temp):
            # Krok 4: Wygeneruj sąsiada
            nowe_rozwiazanie = generuj_sasiada(aktualne_rozwiazanie, procesory)
            nowy_koszt = oblicz_cmax(nowe_rozwiazanie, czasy, procesory)
            
            # Krok 5: Oblicz różnicę kosztu (Delta E)
            delta_kosztu = nowy_koszt - aktualny_koszt
            
            # Krok 6: Podejmij decyzję o akceptacji
            if delta_kosztu < 0:
                # Jeśli nowe rozwiązanie jest lepsze, zawsze je akceptuj
                aktualne_rozwiazanie = nowe_rozwiazanie
                aktualny_koszt = nowy_koszt
                
                # Zaktualizuj najlepsze globalne rozwiązanie, jeśli to konieczne
                if nowy_koszt < najlepszy_koszt:
                    najlepsze_rozwiazanie = nowe_rozwiazanie
                    najlepszy_koszt = nowy_koszt
            else:
                # Jeśli nowe rozwiązanie jest gorsze, akceptuj je
                # z prawdopodobieństwem P = exp(-delta / T)
                p_akceptacji = math.exp(-delta_kosztu / T)
                if random.random() < p_akceptacji:
                    aktualne_rozwiazanie = nowe_rozwiazanie
                    aktualny_koszt = nowy_koszt
                    
        # Krok 7: Schładzanie
        T *= alfa
        
    # Krok 8: Zwróć najlepsze znalezione rozwiązanie
    return najlepszy_koszt, najlepsze_rozwiazanie