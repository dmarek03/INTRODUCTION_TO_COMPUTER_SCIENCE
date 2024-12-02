"""
Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.
"""


def get_sqrt_newton_method_with(number: int) -> int:
    a = 1
    b = ((number/a) + a) / 2
    eps = 10e-6
    while abs(b - a) > eps:
        a, b = b, ((number/b) + b) / 2
    return a

print(get_sqrt_newton_method_with(81))
