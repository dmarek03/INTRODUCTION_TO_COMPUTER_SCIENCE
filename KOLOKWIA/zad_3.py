"""Z liczby binarnej na dziesiętną"""


def change_to_dec(number: int) -> int:
    n_abs = abs(number)
    new_number = 0
    mult = 1
    while n_abs > 0:
        new_number += mult * (n_abs % 10)
        n_abs //= 10
        mult *= 2
    return new_number


#print(change_to_dec(1011))


"""Zamien liczbe na dowlony system"""

def change_to_system(number:int, system: int):

    chars = [str(n) for n in range(0, 10)] + [chr(n) for n in range(ord('A'), ord('F') + 1)]
    new_number = ''
    n_abs = abs(number)

    while n_abs > 0:
        new_number += chars[n_abs % system]
        n_abs //= system

    return new_number[::-1]


# print(change_to_system(123567, 16))
# print(hex(123567))



def is_palindrome(word: str) -> bool:
    n = len(word)
    s = 0
    k = n - 1
    while s < k:
        if word[s] != word[k]:
            return False
        s += 1
        k -= 1
    return True



print(is_palindrome('kajak'))

