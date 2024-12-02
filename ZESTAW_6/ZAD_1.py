"""
Zadanie 1. Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
cyfry.

"""
import math


def is_prime(n: int) -> bool:

    if n < 2:
        return False

    if n in [2, 3]:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def get_len(n: int) -> int:
    return int(math.floor(math.log(n,10)) + 1)


def zad_1(n: int, a=0, p=1, flag=False):

    if n == 0:
        if flag and is_prime(a) and a > 9:
            print(a)
        return
    zad_1(n // 10, a + (n % 10) * p, p * 10, flag) # Bierzemy cyfrę
    zad_1(n // 10, a, p, True) # Nie bierzemy, ale równocześnie naszą liczbę zmniejszamy o jedną cyfre


print(zad_1(1231))