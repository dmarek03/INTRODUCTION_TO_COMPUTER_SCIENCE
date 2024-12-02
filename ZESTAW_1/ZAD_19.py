"""
Zadanie 19. Napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! + 1/1! +
1/2! + 1/3! + ..
"""
from math import factorial


def find_e_value(precision: int) -> float:
    e1 = 1
    for i in range(1, precision):
        e1 += 1 / factorial(i)
    return e1

print(find_e_value(100))
