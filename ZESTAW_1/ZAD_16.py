"""
Zadanie 16. Dany jest ciąg określony wzorem: An+1 = (An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Napisać program, który znajdzie wyraz
początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków.

"""

def find_best_element() -> int:
    best_num = 0
    best_counter = 0

    for start_a in range(2, 10000):
        a = start_a
        counter = 0
        while abs(a - 1) > 10e-6:
            a = (a % 2) * (3 * a + 1) + (1 - a % 2) * (a / 2)
            counter += 1
        if counter > best_counter:
            best_counter = counter
            best_num = start_a
    return best_num

print(find_best_element())

