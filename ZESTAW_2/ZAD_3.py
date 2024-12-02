"""
Zadanie 3. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.
"""
import re


def get_int_number(message: str) -> int:
    while not re.match(r'\d+', text := input(f'{message}:\n')):
        ...
    return int(text)


def is_palindrome(n: int) -> bool:
    reversed_number = 0
    n_abs = abs(n)
    while n_abs > 0:
        reversed_number = 10 * reversed_number + n_abs % 10
        n_abs //= 10
    return reversed_number == n


def is_palindrome_in_bin_system(n: int) -> bool:
    reversed_number = 0
    n_abs = abs(n)
    while n_abs > 0:
        reversed_number = 2 * reversed_number + n_abs % 2
        n_abs //= 2
    return reversed_number == n


def main() -> None:
    number = get_int_number('Enter int number')
    print(f'{number = }')
    print(is_palindrome(number))
    print(is_palindrome_in_bin_system(number))


if __name__ == '__main__':
    main()




