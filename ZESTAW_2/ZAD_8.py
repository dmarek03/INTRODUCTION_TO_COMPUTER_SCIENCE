"""
Zadanie 8. Dana jest N-elementowa tablica t zawierająca liczby naturalne. W tablicy możemy przeskoczyć
z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby t[k]. Napisać funkcję
sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.

"""

"""

[1,4,5,7,8,9,0,4,5,4,7]
"""


def zad_8(t: list[int]) -> bool:
    n = len(t)
    t1 = [False for _ in range(n)]
    t1[0] = True
    for i in range(n):
        if t1[i]:
            k = 2
            while t[i] > 1:
                while t[i] % k == 0:
                    if i + k < n:
                        t1[i + k] = True
                    t[i] //= k
                k += 1

    return t1[-1]


def main() -> None:
    numbers = [2, 9, 81, 34, 2, 6, 78, 8, 9, 9, 5, 6]
    print(zad_8(numbers))

if __name__ == '__main__':
    main()



