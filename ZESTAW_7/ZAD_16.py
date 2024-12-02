"""
16. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jednokierunkowej, przenosi
na początek listy te z nich, które mają parzystą ilość piątek w zapisie ósemkowym.
"""
from list_opperations import *


def count_fives(n: int, base: int, value: int):
    n_abs = abs(n)
    cnt = 0

    while n_abs > 0:
        d = n_abs % base
        if d == value:
            cnt += 1
        n_abs //= base
    return cnt % 2 == 0

print(count_fives(5, 8, 5))
print(hex(5))
def zad_16(head, base, val):
    if not head:
        return None

    node = head

    while node and node.next:
        prev = node

        node = node.next
        if count_fives(node.val, base, val):
            prev.next = node.next
            node.next = head
            head = node
            node = prev

    return head


print_all(zad_16(create_list([5,5,5,12,13,25]),8, 5))

