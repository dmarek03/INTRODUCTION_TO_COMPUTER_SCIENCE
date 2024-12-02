"""
Zadanie 6. Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby
naturalne. Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z
tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2
powinny zawierać zera
"""
from collections import Counter


def get_singletons(t1: list[list[int]]):
    n = len(t1)
    t2 = [0 for _ in range(n*n)]
    m = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if t1[i][j] != t1[k][l]:
                        t2[m] = t1[i][j]
                        m += 1
    return t2


def zad_6(t):
    n = len(t)
    t3 = [0 for _ in range(n * n)]
    m = 0

    for i in range(n):
        for j in range(n):
            t3[m] = t[i][j]
            m += 1

    cnt = Counter()
    for x in t3:
        cnt[x] += 1
    print(cnt.items())

    return sorted([k for k, v in cnt.items() if v == 1])


def main() -> None:
    t = [
        [1, 2, 4, 8, 0],
        [21, 1, 6, 7, 8],
        [1, 2, 4, 5, 7],
        [1, 3, 75, 8, 9],
        [2, 3, 4, 7, 8]

    ]
    print(zad_6(t))


if __name__ == '__main__':
    main()
