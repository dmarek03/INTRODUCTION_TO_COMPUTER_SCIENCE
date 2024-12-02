"""
Zadanie 3. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
parzystą
"""


def has_even_digits(n: int) -> bool:
    n_abs = abs(n)
    while n_abs > 1:
        if n_abs % 10 % 2 == 0:
            return True
        n_abs //= 10
    return False


def zad_3(t: list[list[int]]):
    return any([all([has_even_digits(x) for x in row]) for row in t])


def main() -> None:

    t = [
        [1, 3, 1, 1, 1],
        [2, 4, 5, 4, 7],
        [1, 3, 1, 3, 7],
        [1, 16, 3, 6, 7],
        [2, 4, 8, 16, 2]

    ]

    print(zad_3(t))


if __name__ == '__main__':
    main()
