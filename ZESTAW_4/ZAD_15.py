"""
Zadanie 15. Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy w tablicy istnieje wiersz, w którym każda liczba zawiera co najmniej jedną cyfrę
będącą liczbą pierwszą?
"""


def has_prime_digits(n: int) -> bool:
    n_abs = abs(n)
    while n_abs > 1:
        d = n_abs % 10
        if d in [2, 3, 5, 7]:
            return True
        n_abs //= 10
    return False


def zad_15(t: list[list[int]]):
    n = len(t)

    for i in range(n):
        flag = True
        for j in range(n):
            if not has_prime_digits(t[i][j]):
                flag = False
                break
        if flag:
            return True


def zad_15_2(t: list[list[int]]):
    n = len(t)

    for i in range(n):
        if all([has_prime_digits(x) for x in t[i]]):
            return True
    return False


def zad_15_3(t: list[list[int]]):
    # all -> sprawdza czy  kazdy x w wierszu  ma przynajmaniej jedna cyfre ktora jest liczba pierwsza
    # w drugim list comprehension iterujemy po wierszach w tablicy t
    # any -> sprawdza czy którykoliwek z wierszy spełnia warunek
    return any([all([has_prime_digits(x) for x in row]) for row in t])


T = [
    [2, 3, 4, 5, 12],
    [2, 4, 5, 4, 7],
    [2, 4, 8, 6, 4],
    [1, 16, 8, 16, 7],
    [32, 4, 8, 16, 32]
    ]
print(zad_15_2(T))
