"""
Zadanie 10. Rekurencyjne obliczanie wyznacznika z macierzy (treść oczywista)

"""


def zad_10(t,w=0, k=0, i=0):
    if i == len(t) ** 2:
        return 1

    return (-1) ** (w + k) * zad_10(t, w + i, k + i,  i + 1)

matrix = [ [1,0,1],
           [1,0,1],
           [1,0,1]
         ]

print(zad_10(matrix))
