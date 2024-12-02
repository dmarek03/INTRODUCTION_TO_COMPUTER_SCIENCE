"""
Zadanie 12. Napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb
"""


def get_nwd_3(a: int, b: int, c: int) -> int:
    if b != 0:
        return get_nwd_3(b, a % b, c)
    if c != 0:
        return get_nwd_3(a, c, b % c)
    return a

print(get_nwd_3(10, 4, 12))
