"""
Zadanie 1. Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami
naturalnymi po spirali.
"""


def print_tab(tab):
    for line in tab:
        print(line)
    print("--------------")


def main() -> None:
    n = int(input('Enter size of list:\n'))
    tab = [[0]*n for _ in range(n)]
    print_tab(tab)
    counter = 1
    for row in range(n):
        for _ in range(4):
            for x in range(n):
                if tab[row][x] == 0:
                    tab[row][x] = counter
                    counter += 1
            print_tab(tab)
            tab = [[tab[k][j] for k in range(n)] for j in range(n - 1, -1, -1)]
    # tab = [[tab[w][p] for w in range(n - 1, -1, -1)] for p in range(n)]


    print_tab(tab)

if __name__ == '__main__':
    main()
