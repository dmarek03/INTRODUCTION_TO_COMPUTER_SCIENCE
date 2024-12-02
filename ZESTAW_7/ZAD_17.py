"""
17. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
początek listy dwukierunkowej, usuwa z niej wszystkie elementy, w których
wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.
"""
from list_opperations import *
class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def has_odd_n_of_ones(n: int, base: int) -> bool:
    n_abs = abs(n)
    cnt = 0
    while n_abs > 0:
        if (n_abs % base) % 2 == 1:
            cnt += 1
        n_abs //= base
    return cnt % 2 == 1


def delete(head):

    if head is None:
        raise ValueError('List is empty')

    if head.next is None and has_odd_n_of_ones(head.val, 2):
        return None

    while head is not None and has_odd_n_of_ones(head.val, 2):
        head = head.next
    print(head.val)

    node = head
    i = head
    while i.next is not None:
        i = i.next
        if not has_odd_n_of_ones(i.val, 2):
            node.next = i
            node = node.next

    node.next = None

    return node


list = create_list([2, 2, 1, 4, 3, 12, 14, 4, 1,44])

delete(list)
print_all(list)
