"""
Zadanie 3. Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej
sumie.
"""

n = int(input('Enter int number:\n'))
a, b = 1, 1
sum1 = 0
while sum1 < n:
    sum1 += a
    a, b = b, a + b

while sum1 > n:
    sum1 -= a
    a, b = b, a + b

print(True if sum1 == n else False)





