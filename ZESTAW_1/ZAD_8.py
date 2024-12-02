"""
Zadanie 8. Napisać program sprawdzający czy zadana liczba jest pierwsza.

"""

import re

def get_int_number(message: str) -> int:
    while not re.match(r'\d+', text := input(f'{message}:\n')):
        ...
    return int(text)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in [2, 3]:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** i < n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main() -> None:
    number = get_int_number('Enter int number')
    print(f'{number = }')
    print(is_prime(number))


if __name__ == '__main__':
    main()





