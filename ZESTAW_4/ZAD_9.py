"""
Zadanie 9. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która w
poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.
"""


def zad_9(t: list[list[int]], k: int) -> tuple[int, int, int, bool]:
    n = len(t)
    # Interujemy tylko do n-2 bo jesli mamy mieć kwadrat o nieparzystmy boku większym od 1 to będzie to kwadrat o boku
    # co najmnniej 3 zatem sprawdzamy do n-2 pozycji w liście
    for i in range(n-2):
        for j in range(n-2):
            # szukamy kwadratów o nieparzystmy boku zatem zaczynamy od side = 2 bo lista indeksuje się od zera!!!
            side = 2
            while side + i < n and side + j < n:
                # Tworzymy iloczyn z narozników kwadratu
                product = t[i][j] * t[i][j + side] * t[i + side][j] * t[i + side][j + side]
                if product == k:
                    # Wspolrzedne srodka kwaradtu to suma wspołrzednych konca i poczatku boku podzielona
                    # całkowitoliczbowo przez 2
                    return side + 1, (2*i + side) // 2, (2*j + side) // 2, True
                # Bok zwiększamy o 2 bo interesuja nas kwadraty o nieparzytch bokach
                side += 2
    return -1, -1, -1, False


def main() -> None:
    t = [
        [1, 3, 1, 1, 2],
        [2, 4, 5, 4, 7],
        [1, 3, 1, 3, 7],
        [1, 16, 3, 6, 7],
        [2, 4, 8, 16, 2]

    ]

    print(zad_9(t, 27))


if __name__ == '__main__':
    main()