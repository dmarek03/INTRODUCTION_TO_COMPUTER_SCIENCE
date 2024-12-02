"""
Zadanie 8. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która w
poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego
co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić informacje czy udało
się znaleźć taki ciąg oraz długość tego ciągu.
"""
"""
b**2 == a*c
"""


def diagonal(i: int, j: int, n: int, t: list[list[int]]):
    # sprawdzamy najpierw ciąg po przekątnej
    # szukamy najdłuższego podciągu po głównej przekątnej
    # ciąg geometryczny czyli sprawdzamy q dla dwóch pierwszych wyrazów , tworzymy zmienną prev_q którą potem
    # porównujemy z q dla kolejnych dwóch wyrazów i jeśli są takie same to counter zwiększamy o 1, jeśli sa rózne
    # to counter ustawaimy na 1, za prev_q podstawiamy q i sprawdzmy czy moze dla nowego q bedzie spełniony warunek
    a = t[i][j]
    b = t[i + 1][j + 1]
    prev_q = b / a
    counter = 1
    max_diagonal = 1
    while i < n - 1 and j < n - 1:
        a = t[i][j]
        b = t[i + 1][j + 1]
        q = b / a
        if q == prev_q:
            counter += 1
            # if counter > max_diagonal:
            #     max_diagonal = counter
            max_diagonal = max(max_diagonal, counter)
        else:
            counter = 1
        prev_q = q
        i += 1
        j += 1
    return max_diagonal


def zad_8(t: list[list[int]]) -> tuple[bool, int]:

    # sprawdzamy czy długośc tablicy większa od 3 dla mniejszej nie ma sensu sprawdzać
    n = len(t)
    if n < 3:
        return False, 0
    # Sprawdzamy najpierw dla pierwszego wiersza zatem przechodzimy w pętli po kolmnach do n - 2 kolumny,, po potem
    # i tak nie bedzie spelniomy warunek
    # sprawdzamy w pętli wszystkie przekatne dla 0 wiersza i znajdujemy najdłuszy ciąg spełnaiąjcy warunek
    max_sequence_length = 1
    for j in range(n-2):
        diagonal_counter = diagonal(0, j, n, t)
        # if diagonal_counter > max_sequence_length:d
        #     max_sequence_length = diagonal_counter
        max_sequence_length = max(diagonal_counter, max_sequence_length)
    # tutaj szukamy ciagu po kolmnach zaczynając od pierwszej do n-2 i tez znajdujemy najdłuszy ciag spełnaijacy warunek
    for i in range(1, n - 2):
        diagonal_counter = diagonal(i, 0, n, t)
        # if diagonal_counter > max_sequence_length:
        #     max_sequence_length = diagonal_counter
        max_sequence_length = max(diagonal_counter, max_sequence_length)

    return max_sequence_length >= 3, max_sequence_length


def main() -> None:
    t = [
        [2, 3, 4, 5, 2],
        [2, 4, 5, 4, 7],
        [2, 4, 8, 6, 4],
        [1, 16, 8, 16, 7],
        [32, 4, 8, 16, 32]
        ]

    print(zad_8(t))


if __name__ == '__main__':
    main()
