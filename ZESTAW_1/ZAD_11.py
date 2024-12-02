"""
Zadanie 11. Napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona
"""
from typing import Final


def find_amicable_numbers_le_than(limit: int):

    def get_divisors_sum(n: int) -> int:
        i = 2
        s = 1
        while i * i < n:
            if n % i == 0:
                s += i
            ii = n // i
            if n % ii == 0:
                s += ii
            i += 1
        if i * i == n:
            s += i
        return s
    for n1 in range(1, limit + 1):
        n2 = get_divisors_sum(n1)
        if n2 > n1 == get_divisors_sum(n2):
            print(n1, n2)





def main() -> None:
    LIMIT: Final = 1000000
    print(find_amicable_numbers_le_than(LIMIT))



if __name__ == '__main__':
    main()

