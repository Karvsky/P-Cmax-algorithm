from benchmark import generuj_dane_automatycznie
from przydzial_procesow import answer

generuj_dane_automatycznie()
lista = answer()
for i in range(len(lista)):
    print(lista[i])

