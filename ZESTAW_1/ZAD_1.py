"""
Zadanie 1. Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.
"""


def show_fib_elements_lower_than(n: int):
    a = b = 1
    while a < n:
        print(f'{a}')
        a, b = b, b + a


def main() -> None:
    n = 1000000
    show_fib_elements_lower_than(n)


if __name__ == '__main__':
    main()
