"""
Zadanie 2. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
z nieparzystych cyfr
"""
import math


def get_length_of(num: int) -> int:
    return math.floor(math.log(num, 10)) + 1


def has_odd_digit(number: int) -> bool:
    n_abs = abs(number)
    while n_abs > 1:
        flag = True
        if (n_abs % 10) % 2 == 0:
            flag = False
            break
        n_abs //= 10
        if flag:
            return True


def has_odd_digit_2(n: int):
    n_abs = abs(n)
    digits = [True for _ in range(get_length_of(n))]
    i = 0
    while n_abs > 1:
        if (n_abs % 10) % 2 == 1:
            digits[i] = True
        else:
            digits[i] = False
        n_abs //= 10
        i += 1
    return all(digits)


def zad_1(t: list[list[int]]) -> bool:
    return all([any([has_odd_digit(x) for x in row]) for row in t])


def main() -> None:
    t = [
        [1, 3, 1, 1, 2],
        [2, 4, 5, 4, 7],
        [1, 3, 1, 3, 7],
        [1, 16, 3, 6, 7],
        [5, 4, 8, 16, 2]

    ]

    print(zad_1(t))


if __name__ == '__main__':
    main()