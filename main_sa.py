from benchmark import generuj_dane_automatycznie
from wczytanie_z_pliku import wczytaj_dane_z_pliku
from przydzial_procesow import answer as algorytm_zachlanny
from simulated_annealing import symulowane_wyzarzanie

def formatuj_wynik_sa(rozwiazanie, czasy, procesory):
    lista_przydzialu = [[] for _ in range(procesory)]
    for i in range(len(czasy)):
        maszyna = rozwiazanie[i]
        lista_przydzialu[maszyna].append(czasy[i])
    return lista_przydzialu

T_START = 1000.0   # Wysoka temperatura początkowa
T_STOP = 0.1       # Niska temperatura końcowa
ALFA = 0.99        # Współczynnik schładzania (wolniejsze schładzanie = lepsze wyniki, ale dłużej)
ITERACJE_NA_TEMP = 100 # Liczba prób na każdym poziomie temperatury

generuj_dane_automatycznie(max_procesorow=10, max_procesow=200, max_czas_zadania=50)
dane = wczytaj_dane_z_pliku()

if not dane:
    print("Nie udało się wczytać danych. Koniec programu.")
    exit()

procesory = dane[0]
procesy = dane[1] # Liczba procesów
czasy = dane[2:]  # Lista czasów wykonania zadań

print(f"Wygenerowano problem: {procesory} maszyny, {procesy} zadań.")
print("-" * 40)

Cmax_zachlanny, lista_zachlanna = algorytm_zachlanny()
print(f"Wynik algorytmu zachłannego (List Scheduling):")
print(f"C||max: {Cmax_zachlanny}")

print("-" * 40)

print("Uruchamianie Symulowanego Wyżarzania (może chwilę potrwać)...")
Cmax_sa, rozwiazanie_sa = symulowane_wyzarzanie(
    czasy,
    procesory,
    T_START,
    T_STOP,
    ALFA,
    ITERACJE_NA_TEMP
)

print(f"Wynik algorytmu Symulowanego Wyżarzania (SA):")
print(f"C||max: {Cmax_sa}")

lista_sa = formatuj_wynik_sa(rozwiazanie_sa, czasy, procesory)

print("-" * 40)

print("\n--- PODSUMOWANIE ---")
print(f"Oryginalny Cmax (zachłanny): {Cmax_zachlanny}")
print(f"Nowy Cmax (SA):             {Cmax_sa}")

poprawa = Cmax_zachlanny - Cmax_sa
if poprawa > 0:
    procent_poprawy = (poprawa / Cmax_zachlanny) * 100
    print(f"Poprawa: {poprawa} (lepszy o {procent_poprawy:.2f}%)")
elif poprawa < 0:
    print(f"Algorytm SA znalazł gorsze rozwiązanie ({abs(poprawa)}). Spróbuj dostosować parametry.")
else:
    print("Algorytm SA nie znalazł lepszego rozwiązania.")