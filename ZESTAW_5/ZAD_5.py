"""
Zadanie 5. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada na pytanie
czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość każdego z kawałków nie
może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu 110100 nie jest możliwe.
"""

def is_prime(x):
    if x < 2:
        return False
    if x in [2, 3]:
        return True

    if x % 2 == 0 or x % 3 == 0:
        return False

    i = 5
    while i ** 2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6

    return True


def consists_of_primes(t, p=0, how_pieces_1=1):
    if p == len(t):
        return False, how_pieces_1
    if 2 < how_pieces_1 < 31:
        return True, how_pieces_1

    i = 1
    x = t[p]
    while p + i < len(t):
        x += t[i + p] * (2 ** i)
        print(x)
        if is_prime(x):
            print(x)

            if p + i < len(t) - 1: # spr czy kawalek konczy sie na koncu tablicy
                is_of_primes, how_pieces_1 = consists_of_primes(t, p + i + 1, how_pieces_1 + 1)
                if is_of_primes:
                    return True, how_pieces_1
            else:
                return True, how_pieces_1
        i += 1
    return False, how_pieces_1



t = [1,1,0,0,1, 1]



print(consists_of_primes(t))
