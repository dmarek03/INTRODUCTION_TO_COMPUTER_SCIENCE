"""
Zadanie 10. Napisać program wyszukujący liczby doskonałe mniejsze od miliona
"""

from typing import Final


def find_prefect_number_le_than(limit: int) -> None:

    def get_divisors_sum(n: int) -> int:

        i = 2
        divisors_sum = 1
        while i * i < n:
            if n % i == 0:
                divisors_sum += i

            ii = n // i
            if n % ii == 0:
                divisors_sum += ii
            i += 1
        if i * i == n:
            divisors_sum += i
        return divisors_sum
    for n in range(2, limit + 1):
        if get_divisors_sum(n) == n:
            print(n)


def main() -> None:
    LIMIT: Final = 100000
    print(find_prefect_number_le_than(LIMIT))


if __name__ == '__main__':
    main()
