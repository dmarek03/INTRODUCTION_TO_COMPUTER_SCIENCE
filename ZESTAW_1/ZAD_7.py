"""
Zadanie 7. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.

"""
import re


def get_int_number(message: str) -> int:
    while not re.match(r'\d+', text := input(f'{message}:\n')):
        ...
    return int(text)


def is_product_of_fib_elements(number: int) -> bool:
    a, b = 1, 1

    while a * b < number:
        a, b = b, a + b

    if a * b == number:
        return True
    return False


def main() -> None:
    number = get_int_number('Enter number')
    print(f'{number = }')
    print(f'{number} is the product of two following words of the Fibonacci number => {is_product_of_fib_elements(number)}')


if __name__ =='__main__':
    main()


