"""
Zadanie 8. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy.
Odważniki można umieszczać  na obu szaklach.
"""


def zad_8(t1, mass, i=0,):

    if mass == 0:
        return True

    if i == len(t1):
        return False

    return zad_8(t1, mass, i + 1) or zad_8(t1, mass - t1[i], i + 1) or zad_8(t1, mass + t1[i], i + 1)


t = [2, 3, 5, 10]


print(zad_8(t, 14))

