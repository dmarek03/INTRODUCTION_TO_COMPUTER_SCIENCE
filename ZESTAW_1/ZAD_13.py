"""
Zadanie 13. Napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb
"""


def get_nwd(a: int, b: int) -> int:
    if b != 0:
        return get_nwd(b, a % b)
    return a


def get_nww(a: int, b: int) -> int:
    return (a * b) // get_nwd(a, b)


def get_nww3(a: int, b: int, c: int) -> int:
    return get_nww(get_nww(a, b), c)

print(get_nww3(4, 12, 10))