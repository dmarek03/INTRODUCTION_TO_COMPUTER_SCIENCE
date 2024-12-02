"""
Zadanie 5. Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakończonych
zerem stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.
"""

import re


def get_sequence_until_ends_with(number: int) -> list[int]:

    def get_int_number(message: str):
        while not re.match(r'^\d+$', text := input(f'{message}:\n')):
            ...
        return int(text)
    new = []
    while (n := get_int_number('Enter int number')) != number:
        new.append(n)
    return new


def find_kth_max_number(k: int, numbers: list[int]) -> int:
    return sorted(set(numbers), reverse=True)[k-1]


def main() -> None:
    numbers = get_sequence_until_ends_with(0)
    print(f'{numbers = }')
    print(find_kth_max_number(10, numbers))


if __name__ == '__main__':
    main()
