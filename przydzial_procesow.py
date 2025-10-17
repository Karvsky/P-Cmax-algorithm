from wczytanie_z_pliku import wczytaj_dane_z_pliku

def answer():
    dane = wczytaj_dane_z_pliku()

    procesory = dane[0]
    procesy = dane[1]
    czasy = dane[2:]

    przydzial_czasowy = []
    przydzial_elementowy = []
    for i in range(procesory):
        przydzial_czasowy.append(czasy[i])
        przydzial_elementowy.append([czasy[i]])

    for i in range(procesory, procesy):
        minimalna = min(przydzial_czasowy)
        index_minimalna = przydzial_czasowy.index(minimalna)
        przydzial_czasowy[index_minimalna] += czasy[i]
        przydzial_elementowy[index_minimalna].append(czasy[i])

    return max(przydzial_czasowy), przydzial_elementowy

