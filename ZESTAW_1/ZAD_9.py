"""
Zadanie 9. Napisać program wypisujący podzielniki liczby.

"""
import math


def show_divisors_of(number: int) -> None:

    if number == 0:
        print(f'Each number except of 0 is a divisor of {number}')

    i = 1
    while i * i < number:
        if number % i == 0:
            print(i)
            print(-i)
            print(number // i)
            print(-number // i)
        i += 1
    if i * i == number:
        print(i)
        print(-i)


print(show_divisors_of(100))











