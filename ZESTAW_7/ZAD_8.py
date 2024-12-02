"""
8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi element listy.
Do funkcji należy przekazać wskazanie na pierwszy element listy.
"""

from list_opperations import *


def delete_2(head):
    if head is None:
        return None

    node = head

    while node and node.next is not None:
        node.next = node.next.next
        node = node.next
    return head


if __name__ == '__main__':

    p3 = Node(2)
    p3 = append(p3, 5)
    p3 = append(p3, 3)
    p3 = append(p3, 8)
    p3 = append(p3, 9)
    p3 = delete_2(p3)
    q3 = Node(1)
    q3 = append(q3, 12)
    q3 = delete_2(q3)
    print_all(delete_2(None))
    print_all(p3)
    print_all(q3)
