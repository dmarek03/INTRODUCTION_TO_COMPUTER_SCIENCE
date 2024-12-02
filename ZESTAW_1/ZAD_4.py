"""
Zadanie 4. Proszę napisać program obliczający pierwiastek całkowitoliczbowy z liczby naturalnej korzystając z zależności
 1 + 3 + 5 + ... = n ^ 2
"""

s = int(input('Enter int number:\n'))
sum1 = 0
n = 0
a1 = 0

while sum1 <= s:
    sum1 += a1
    n += 1
    a1 += 2
print(n-1)