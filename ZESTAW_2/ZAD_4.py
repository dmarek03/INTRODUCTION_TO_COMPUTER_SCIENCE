"""
Zadanie 4. Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż
2,3,5. Jedynka też jest taką liczbą. Napisz program, który wylicza ile takich liczb znajduje się w przedziale
od 1 do N włącznie.
"""

from typing import Final


def find_number_prime_elements(number: int):
    i = 1
    new = []
    while i ** 2 < number:
        if number % 3 == 0 or number % 5 == 0 or number % 2 == 0:
            new.append(number)
        ii = number // 3
        ii2 = number // 2
        ii3 = number // 5
        if number // ii ==


print(find_number_prime_elements(17))
def count_two_three_five_numbers_in_range(r_min: int, r_max: int) -> int:
    ...