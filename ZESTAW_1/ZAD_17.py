"""
Zadanie 17. Napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych wyrazów
ciągu Fibonacciego. Wyznaczyć ten iloraz dla różnych wartości początkowych wyrazów ciągu.
"""


def find_golden_ratio() -> float:
    a, b = 1, 1
    old_ratio, ratio = 1, 0
    while abs(old_ratio - ratio) > 10e-8:
        a, b = b, a + b
        old_ratio, ratio = ratio, b / a
    return b / a

print(find_golden_ratio())