"""
7. Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji należy przekazać wskazanie na pierwszy element
listy.
"""
from list_opperations import Node, append, print_all


def delete_last(head):
    if head is None:
        raise ValueError('Cannot delete element from empty list')
    if head.next is None:
        return None

    node = head
    while node.next is not None:
        prev = node
        node = node.next

    prev.next = None
    return head


if __name__ == '__main__':
    p1 = Node(1)
    p1 = append(p1, 2)
    p1 = append(p1, 4)

    p1 = delete_last(p1)
    print_all(p1)
    #
    # q1 = Node(6)
    # q1 = delete_last(q1)
    # print_all(q1)
    # q2 = None
    # q2 = delete_last(q2)
