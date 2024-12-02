"""
Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy.
Odważniki można umieszczać na obu szalkach. Program powinien wypisywać wybrane odważniki.
"""


def zad_9_r(t1, m, w1, w2, i=0):
    if m == 0:
        print(w1, w2)
        return True
    if i == len(t1):
        return False

    return zad_9_r(t1,m, w1, w2, i + 1) or zad_9_r(t1,m - t1[i], w1 + [t1[i]], w2, i + 1) or zad_9_r(t1, m + t1[i], w1,
                                                                                               w2 + [t1[i]], i + 1)


t = [1, 2, 3, 5, 10]
print(zad_9_r(t, 16, [], []))


