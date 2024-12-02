"""
Zadanie 2. Napisać program wczytujący trzy liczby naturalne a,b,n i wypisujący rozwinięcie dziesiętne
ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej . (n jest rzędu 100)

"""

import re


def get_three_int_number()-> tuple[int, int, int]:

    def get_int_number(message: str) -> int:
        while not re.match(r'\d+', text := input(f'{message}:\n')):
            ...
        return int(text)

    a = get_int_number('Enter first number')
    b = get_int_number('Enter second number')
    n = get_int_number('Enter third number')

    return a, b, n


def count_decimal_expansion_of_fraction_with_precision_to(n: int, a: int, b: int) -> None:

    print(a // b, '.' if a % b != 0 else '', sep='', end='')
    a %= b
    while a > 0 and n > 0:
        a *= 10
        print(a // b, end='')
        a %= b
        n -= 1

print(count_decimal_expansion_of_fraction_with_precision_to(100, 9, 17))

