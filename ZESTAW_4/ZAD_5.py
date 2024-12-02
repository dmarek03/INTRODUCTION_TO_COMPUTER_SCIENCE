"""
Zadanie 5. Dana jest tablica T[N][N] wypełniona liczbami całkowitymi . Proszę napisać funkcję, która
zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
element do sumy elementów wiersza w którym leży element jest największa
"""


def get_rows_columns_sum(t: list[list[int]]) -> tuple[list[int], list[int]]:
    n = len(t)
    rows_sum = [0 for _ in range(n)]
    columns_sum = [0 for _ in range(n)]

    for x in range(n):
        for y in range(n):
            rows_sum[x] += t[x][y]
            columns_sum[x] += t[y][x]

    return rows_sum, columns_sum


def zad_5(t: list[list[int]]):
    rows_sum, columns_sum = get_rows_columns_sum(t)
    n = len(columns_sum)
    max_ratio = 0
    max_ratio_index = (0, 0)
    for x in range(n):
        for y in range(n):
            if rows_sum[x] != 0:
                ratio = columns_sum[y] / rows_sum[x]
                ratio_index = (x, y)
                if ratio > max_ratio:
                    max_ratio = ratio
                    max_ratio_index = ratio_index
            else:
                raise ValueError('Cannot divide by zero!')

    return max_ratio, max_ratio_index


def main() -> None:
    t = [
        [-1.2, 3, 1, 1, 1],
        [-2, 4, 5, 4, 2.6],
        [-1, 3, 1.8, 3, 7],
        [0, 0, 0, 0.0, -1],
        [-2, 4.4, 8, 1, 2.]

    ]
    print(get_rows_columns_sum(t))
    print(zad_5(t))

if __name__ == '__main__':
    main()


