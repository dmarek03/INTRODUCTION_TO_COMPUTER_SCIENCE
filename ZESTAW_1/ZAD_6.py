"""
Proszę napisać program rozwiązujący równanie x
x = 2020 metodą bisekcji
"""


def f(x: float) -> float:
    return x ** x - 2022


def solve() -> float:
    a = 0
    b = 10
    eps = 1e-10
    while abs(b-a) > eps:
        x = (a + b) / 2
        if f(x) > 0:
            b = x
        elif f(x) < 0:
            a = x
    return a

print(solve())