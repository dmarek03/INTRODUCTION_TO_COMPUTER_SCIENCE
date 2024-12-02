"""
Zadanie 6. Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów.
Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.
"""

import math


def zad_6(t, el_s=0, idx_s=0, min_length=math.inf, i=0, l=0):
    if i == len(t):
        return el_s == idx_s and el_s > 0, el_s, l

    best_s = 0
    poss = False

    ans, s, length = zad_6(t, el_s, idx_s, min_length, i + 1, l)
    if ans and length < min_length:
        min_length = length
        best_s = s
        poss = True

    ans, s, length = zad_6(t, el_s + t[i], idx_s + i, min_length, i + 1, l + 1)
    if ans and length < min_length:
        min_length = length
        best_s = s
        poss = True

    return poss, best_s, min_length


t = [1,7,3,5,11,21]
print(zad_6(t))
