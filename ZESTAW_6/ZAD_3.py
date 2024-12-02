"""
Zadanie 3. Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi koszt
przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie k.
Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
polu startowym i ostatnim także wliczamy do kosztu przejścia.
"""
import random


def drawn_matrix(size: int) -> list[list[int]]:
    return [[random.randint(1, 9) for _ in range(size)] for _ in range(size)]


def zad_3(t, k, w=0, s=0):

    if w == 7:
        return t[w][k]

    if 0 < k <= 7:
        left = zad_3(t, k - 1, w + 1, s + t[w][k])
    else:
        left = float('inf')
    if 0 <= k < 7:
        right = zad_3(t, k + 1, w + 1, s + t[w][k])
    else:
        right = float('inf')

    middle = zad_3(t, k, w + 1, s + t[w][k])

    return min(right, middle, left) + t[w][k]


def main() -> None:

    t = drawn_matrix(8)
    print(*t, sep='\n')
    print(f'The cost of the cheaper path is {zad_3(t,0)} ')


if __name__ == '__main__':
    main()
