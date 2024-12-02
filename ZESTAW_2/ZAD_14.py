"""
Zadanie 14. Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić
wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
zadanych liczb.


1 2 3 456

123 456
12 4 3 56
12 45 3 6
12 456 3
1 4 23 56
1 4 2 5 3 6
1 4 2 56 3
1 45 23 6
1 45 2 6 3
1 456 23


456 123



"""

import math
import re


def get_two_int_number() -> tuple[int, int]:

    def get_int_number(message: str) -> int:
        while not re.match(r'\d+', text := input(f'{message}:\n')):
            ...
        return int(text)

    n1 = get_int_number('Enter first number')
    n2 = get_int_number('Enter second number')

    return n1,n2


def is_prime(n: int) -> bool:

    if n < 2:
        return False

    if n in [2, 3]:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def get_length_of(n: int):
    return math.floor(math.log10(n)) + 1


def validate_mask(length1: int, length2: int, mask: int):
    while mask > 0:
        if mask % 2 == 0:
            length1 -= 1
        else:
            length2 -= 1

        mask //= 2

    return length1 >= 0 and length2 == 0


def mix_numbers(a: int, b: int, mask: int):
    new_num = 0
    mult = 1
    while mask > 0 or a > 0:
        if mask % 2 == 0:
            d = a % 10
            a //= 10
        else:
            d = b % 10
            b //= 10

        mask //= 2

        new_num = d * mult + new_num
        mult *= 10

    return new_num


def main() -> None:
    a, b = get_two_int_number()
    counter = 0
    length_a, length_b = get_length_of(a), get_length_of(b)

    for mask in range(2 ** (length_a + length_b)):
        if validate_mask(length_a, length_b, mask) and is_prime(mix_numbers(a, b, mask)):
            counter += 1

    print(counter)

if __name__ == '__main__':
    main()