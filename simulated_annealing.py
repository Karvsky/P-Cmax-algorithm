import random
import math

def oblicz_cmax(przydzial, czasy, procesory):
    if not czasy:
        return 0
    
    obciazenie_procesorow = [0] * procesory
    for i, czas_zadania in enumerate(czasy):
        maszyna = przydzial[i]
        obciazenie_procesorow[maszyna] += czas_zadania
        
    return max(obciazenie_procesorow)

def generuj_rozwiazanie_poczatkowe(czasy, procesory):

    liczba_zadan = len(czasy)
    przydzial = [0] * liczba_zadan 
    obciazenie_procesorow = [0] * procesory

    for i in range(min(procesory, liczba_zadan)):
        przydzial[i] = i
        obciazenie_procesorow[i] = czasy[i]

    for i in range(procesory, liczba_zadan):
        idx_min_obciazenia = obciazenie_procesorow.index(min(obciazenie_procesorow))
        przydzial[i] = idx_min_obciazenia
        obciazenie_procesorow[idx_min_obciazenia] += czasy[i]
        
    return przydzial

def generuj_sasiada(rozwiazanie, procesory):
    if not rozwiazanie:
        return []

    nowe_rozwiazanie = list(rozwiazanie) 
    
    idx_zadania = random.randint(0, len(nowe_rozwiazanie) - 1)
    stara_maszyna = nowe_rozwiazanie[idx_zadania]
    
    nowa_maszyna = random.randint(0, procesory - 1)
    while nowa_maszyna == stara_maszyna and procesory > 1:
        nowa_maszyna = random.randint(0, procesory - 1)
        
    nowe_rozwiazanie[idx_zadania] = nowa_maszyna
    
    return nowe_rozwiazanie

def symulowane_wyzarzanie(czasy, procesory, T_start, T_stop, alfa, iteracje_na_temp):
    
    T = T_start
    
    aktualne_rozwiazanie = generuj_rozwiazanie_poczatkowe(czasy, procesory)
    aktualny_koszt = oblicz_cmax(aktualne_rozwiazanie, czasy, procesory)
    
    najlepsze_rozwiazanie = list(aktualne_rozwiazanie)
    najlepszy_koszt = aktualny_koszt
    
    while T > T_stop:
        for _ in range(iteracje_na_temp):
            nowe_rozwiazanie = generuj_sasiada(aktualne_rozwiazanie, procesory)
            nowy_koszt = oblicz_cmax(nowe_rozwiazanie, czasy, procesory)
            
            delta_kosztu = nowy_koszt - aktualny_koszt
            
            if delta_kosztu < 0:
                aktualne_rozwiazanie = nowe_rozwiazanie
                aktualny_koszt = nowy_koszt
                
                if nowy_koszt < najlepszy_koszt:
                    najlepsze_rozwiazanie = nowe_rozwiazanie
                    najlepszy_koszt = nowy_koszt
            else:
                p_akceptacji = math.exp(-delta_kosztu / T)
                if random.random() < p_akceptacji:
                    aktualne_rozwiazanie = nowe_rozwiazanie
                    aktualny_koszt = nowy_koszt
                    
        T *= alfa
        
    return najlepszy_koszt, najlepsze_rozwiazanie