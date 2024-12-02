"""
Zadanie 1. Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.
"""


def convert_number_to (number: int):
    n_abs = abs(number)
    new = 0
    while n_abs > 0:
        new = n_abs % 2
        n_abs //= 2
    return str(new[::-1])
print(convert_number_to(10))