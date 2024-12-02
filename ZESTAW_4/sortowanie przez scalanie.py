"""
Posortuj tablice przez scalanie
"""
t1 = [2,5,1,8,4]
t2 = [12,3,7,6]
n1 = len(t1)
n2 = len(t2)
sorted_list = [0 for _ in range(n1 + n2)]

i,j = 0, 0
k = 0
while i < n1 and j < n2:
    if t1[i] < t2[j]:
        sorted_list[k] = t1[i]
        i += 1
        k += 1

    else:
        sorted_list[k] = t2[j]
        j += 1
        k += 1

if n1 == i:
    while n2 > j:
        sorted_list[k] = t2[j]
        j += 1
        k += 1

else:
    while n1 > i:
        sorted_list[k] = t1[i]
        i += 1
        k += 1

print(sorted_list)
