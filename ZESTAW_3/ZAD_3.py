"""
Zadanie 3. Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa.

"""
import re


def get_int_number(message: str) -> int:
    while not re.match(r'\d+', text := input(f'{message}:\n')):
        ...
    return int(text)


def sieve_of_eratosthenes(num: int):
    numbers = [n for n in range(num)]
    numbers[0], numbers[1] = False, False
    for i in range(2, num):
        if numbers[i] > 0:
            for j in range(2 * numbers[i], num, numbers[i]):
                numbers[j] = 0

    for el in numbers:
        if numbers[el] > 0:
            print(el)

print(sieve_of_eratosthenes(100))