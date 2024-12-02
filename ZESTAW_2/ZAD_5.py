"""
Zadanie 5. Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera. Ile
różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie. Np.
dla 2315 będą to 21, 35, 231, 315.
"""

"""
mask = 0010
n = 2315
mult = 1
d = 0
d = 1 * 5
n = 231
mult = 10
mask = 001
mask = 00
d = 10 *

"""

import math
import re


def get_int_number(message: str) -> int:
    while not re.match(r'[1-9]+', text := input(f'{message}:\n')):
        ...
    return int(text)


def get_length(num):
    return math.floor(math.log10(num)) + 1


def reduce(n: int, mask: int) -> int:
    mult = 1
    new_number = 0
    while n > 0:
        if mask % 2 == 0:
            d = n % 10
            new_number += mult * d
            mult *= 10
        n //= 10
        mask //= 2
    return new_number


def main() -> None:
    number = get_int_number('Enter  number greater than zero')
    print(number)

    counter = 0
    num_length = get_length(number)
    for mask in range(2 ** num_length - 1):
        if reduce(number, mask) % 7 == 0:
            counter += 1

    print(counter)


if __name__ == '__main__':
    main()











