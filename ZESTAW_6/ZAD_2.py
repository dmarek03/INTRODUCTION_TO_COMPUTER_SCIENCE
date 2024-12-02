"""
Zadanie 2. ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool
"""


def weight(t: list[int]) -> list[int]:

    def count_first_elements(number: int) -> int:
        counter = 0
        i = 2
        while number > 1 and i <= number // 2:
            if number % i == 0:
                counter += 1
                while number % i == 0:
                    number //= i
            i += 1
        return counter

    return [count_first_elements(i) for i in t]


def zad_2(t1: list[int]) -> bool:

    def zad_2_r(s1=0, s2=0, s3=0, i=0):
        if i == len(t1):
            return s1 == s2 == s3

        return zad_2_r(s1 + t_weight[i], s2, s3, i + 1) or \
               zad_2_r(s1, s2 + t_weight[i], s3, i + 1) or \
               zad_2_r(s1, s2, s3 + t_weight[i], i + 1)

    t_weight = weight(t1)
    return zad_2_r() if sum(t_weight) % 3 == 0 else False


t_1 = [1,4,4,4]
print(zad_2(t_1))
