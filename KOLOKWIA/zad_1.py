"""
Wyświetl liczby -100 do 100
"""

# for i in range(-100, 101):
#     print(i)



""" Sprawdz czy liczba jest doskonała"""


def find_divisors_of(num: int) -> int:
    i = 2
    sum = 1
    while i*i <= num:
        if num % i == 0:
            sum += i
            ii = num // i
            if num % ii == 0:
                sum += ii

        if i * i == num:
            sum += i
        i += 1
    return sum

print(find_divisors_of(20))


def divisor_sum(n: int) -> int:


    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum


def is_perfect(number: int) -> bool:
    return divisor_sum(number) == number

# print(is_perfect(6))
#
# print(divisor_sum(6))


"""Wypisz liczby pierwsze od zera do 100"""


def is_prime(n) -> bool:
    if n < 2:
        return False

    if n in [2, 3]:

        return True

    if n % 2 == 0 or n % 3 == 0:

        return False

    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

#
# for i in range(0, 101):
#     if is_prime(i):
#         print(i)
