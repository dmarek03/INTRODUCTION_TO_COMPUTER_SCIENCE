"""
18. Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy unikalne.
Do funkcji należy przekazać wskazanie na pierwszy element listy.
"""
from list_opperations import *


def remove_duplicates(sub_head, value):
    if not sub_head:
        return False, None
    flag = False

    while sub_head and sub_head.val == value:
        sub_head = sub_head.next
        flag = True

    node = sub_head
    prev = None
    while node:
        # pierwsze sprawdzenie to zawsze false, z powodu pierwszej petli
        if node.val == value:
            prev.next = node.next
            node = prev
            flag = True
        prev = node
        node = node.next

    return flag, sub_head


def only_uniq(head):
    if not head:
        return None

    if not head.next:
        return head

    found_duplicate, sublist_head = remove_duplicates(head.next, head.val)
    print(sublist_head.val)
    print(found_duplicate)
    print('-------------------------')

    while head and found_duplicate:
        print(head.val)
        print('-------------------------')
        head = sublist_head
        found_duplicate, sublist_head = remove_duplicates(head.next, head.val)

    if head:
        node = head.next
    while node is not None:
        found_duplicate, sublist_head = remove_duplicates(node.next, node.val)
        if found_duplicate:
            node.next = sublist_head
            node = head
        node = node.next

    return head

p1 = create_list([2,1,9,3,1,5])
print_all(only_uniq(p1))
