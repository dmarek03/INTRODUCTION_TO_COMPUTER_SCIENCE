"""
11. Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do której przekazujemy wskaźnik na początek
oraz wartość klucza. Jeżeli element o takim kluczu występuje w liście należy go usunąć z listy.
Jeżeli elementu o zadanym kluczu brak w liście należy element o takim kluczu wstawić do listy.
"""
from list_opperations import *


def zad_11(head, key):
    if head is None:
        return Node(key)

    if head.val == key:
        return head.next

    node = head

    if head.next is None:
        if head.val == key:
            return None

    while node.next is not None:
        prev = node

        node = node.next
        if node.val == key:
            prev.next = node.next
            return head

    node.next = Node(key)
    return head


a1 = Node(5)
a1 = append(a1, 6)
a1 = append(a1, 8)
a1 = zad_11(a1, 5)
b1 = Node(9)
b1 = zad_11(b1,9)
print_all(a1)
print_all(b1)