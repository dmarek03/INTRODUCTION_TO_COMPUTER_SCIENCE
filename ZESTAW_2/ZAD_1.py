"""
Zadanie 1. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.

"""
import re
import math

def get_int_number(message: str) -> int:
    while not re.match(r'\d+', text := input(f'{message}:\n')):
        ...
    return int(text)


def check_if_number_is_product_of_two_fib_elements(number: int) -> bool:
    a1, a2 = 1, 1
    while a1 ** 2 < number:
        if number % a1 == 0:
            b1, b2 = a1, a2
            while a1 * b1 < number:
                b1,  b2 = b2, b1 + b2

            if a1 * b1 == number:
                return True
        a1, a2 = a2, a1 + a2
    return False









for i in range(1, 100):
    print(f'{i} => {check_if_number_is_product_of_two_fib_elements(i)}')