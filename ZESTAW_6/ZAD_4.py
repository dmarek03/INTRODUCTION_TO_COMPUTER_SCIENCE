"""
Zadanie 4. Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
wymiarach NxN ruchem skoczka szachowego.
"""


def contains(t, w, k) -> bool:
    return (0 <= w < len(t)) and (0 <= k < len(t))


def zad_4(t, w=0, k=0, n=1):
    t[w][k] = n
    if n == len(t) ** 2:
        print(*t, sep='\n')
        return True
    jumps = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]

    for jump in jumps:
        new_w = w + jump[0]
        new_k = k + jump[1]

        if contains(t, new_w, new_k) and t[new_w][new_k] == 0:
            if zad_4(t, new_w, new_k, n + 1):
                return True

    t[w][k] = 0
    return False


t = [[0 for _ in range(5)] for _ in range(5)]

print(zad_4(t))



