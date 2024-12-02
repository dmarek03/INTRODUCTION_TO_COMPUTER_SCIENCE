"""
Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy.
Odważniki można umieszczać tylko na jednej szalce
"""


def zad_7(t,mass, i=0) -> bool:
    if mass == 0:
        return True
    if i == len(t):
        return False

    return zad_7(t, mass, i + 1) or zad_7(t, mass - t[i], i + 1)


t = [2, 3, 5, 10]

print(zad_7(t, 14))
