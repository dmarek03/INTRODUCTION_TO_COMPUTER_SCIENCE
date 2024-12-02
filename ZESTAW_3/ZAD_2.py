"""
Zadanie 2. Napisać funkcje sprawdzającą czy dwie liczby naturalne są one zbudowane z takich samych
cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.
"""
import re


def get_two_int_number():
    def get_int_number(message: str) -> int:
        while not re.match(r'\d+', text := input(f'{message}:\n')):
            ...
        return int(text)
    return get_int_number('Enter first number'), get_int_number('Enter second number')


def get_digits_at(position: int, number: int) -> int:
    if position < 0:
        raise ValueError('Position is out of range')
    return (abs(number) // 10 ** position) % 10


def get_length_of(number: int) -> int:
    n_abs = abs(number)
    cnt = 0
    while n_abs > 0:
        n_abs //= 10
        cnt += 1
    return cnt


def have_same_digits(n1: int, n2: int):
    d1 = [get_digits_at(i, n1) for i in range(get_length_of(n1))]
    d2 = [get_digits_at(i, n2) for i in range(get_length_of(n2))]
    digits = [0] * 10

    for d in d1:
        digits[int(d)] += 1

    for d in d2:
        digits[int(d)] += -1

    for i in range(10):
        if digits[i] != 0:
            return False
    return True


n1, n2 = get_two_int_number()
print(sorted(str(n1)) == sorted(str(n2)))





