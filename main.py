from benchmark import generuj_dane_automatycznie
from przydzial_procesow import answer

generuj_dane_automatycznie()
Cmax, lista = answer()
print('C||max:', Cmax)
for i in range(len(lista)):
    print(f'Mszyna {i + 1}', lista[i])

