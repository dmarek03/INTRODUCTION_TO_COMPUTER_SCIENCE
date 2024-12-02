"""
Zadanie 15. Nieskończony iloczyn sqrt(0.5) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5)) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5 + 0.5 ∗
sqrt(0.5))) ∗ ... ma wartość 2/π. Napisz program korzystający z tej zależności i wyznaczający wartość π.

"""

from math import sqrt

def find_value_of_pi(precision: int) -> float:
    pi = 2
    a = sqrt(0.5)
    for _ in range(precision):
        pi /= a
        a = sqrt(0.5 + 0.5 * a)
    return pi

print(find_value_of_pi(10))