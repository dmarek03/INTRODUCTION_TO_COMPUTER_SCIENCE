"""Zamiana na system binarny"""


def change_to_bin(number: int, base: int):
    new_number = 0
    mult = 1
    n_abs = abs(number)
    while n_abs > 0:
        new_number += mult * (n_abs % base)
        n_abs //= base
        mult *= 10
    return new_number


print(change_to_bin(31, 2))


"""Dwie liczby sa do siebie podbne jesli maja taka sama liczbe zer i jedynek. Sprawdz czy podane liczby sa podobne"""


def check(a, b):
    bin_a = change_to_bin(a, 2)
    bin_b = change_to_bin(b, 2)
    cnt1a = 0
    cnt0a = 0
    cnt1b = 0
    cnt0b = 0
    while bin_a > 0:
        if bin_a % 2 == 0:
            cnt0a += 1
        else:
            cnt1a += 1

        bin_a //= 2

        if bin_b > 0:
            if bin_b % 2 == 0:
                cnt0b += 1
            else:
                cnt1b += 1
            bin_b //= 2

        if cnt0a > cnt0b and len(str(bin_a)) < len(str(bin_b)):
            return False

        if cnt1a > cnt1b and len(str(bin_a)) < len(str(bin_b)):
            return False

    return cnt0a == cnt0b and cnt1a == cnt1b

print(check(31, 31))


