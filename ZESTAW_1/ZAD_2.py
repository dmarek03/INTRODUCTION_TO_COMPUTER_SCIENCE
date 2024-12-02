"""
Zadanie 2. Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, aby w ciągu analogicznym
do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.
"""

suma = 10000
best = 2020, 0

for i in range(2021):
    y = 2020
    x = i
    while 0 < x < y:
        x, y = y - x, x
    if x + y < suma:
        suma = x + y
        best = x, y

print(suma)
print(best)
