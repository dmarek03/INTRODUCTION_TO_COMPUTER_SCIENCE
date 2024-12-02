"""
Zadanie 5. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
110100 nie jest możliwe.

"""

def is_prime(n: int) -> bool:

    if n < 2:
        return False

    if n in [2, 3]:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def zad_5(t, parts=0, p=0) -> bool:

    if p == len(t):
        if parts < 31:
            return True

    i = 1
    x = t[p]
    while p + i < len(t):
        x += t[p + i] * (2 ** i)
        if is_prime(x):
            if p + i + 1 < len(t):
                if zad_5(t, parts + 1, p + i + 1):
                    return True
            elif parts > 2:
                return True
        i += 1
    return False


t1 = [1,1,0]
print(zad_5(t1))
