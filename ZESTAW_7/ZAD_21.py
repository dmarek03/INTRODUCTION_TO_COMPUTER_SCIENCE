"""
21. Kolejne elementy listy o zwiększającej się wartości pola val nazywamy podlistą rosnącą. Proszę napisać funkcję,
która usuwa z listy wejściowej najdłuższą podlistę rosnącą. Warunkiem usunięcia jest istnienie w liście dokładnie jednej
najdłuższej podlisty rosnącej.
"""
from list_opperations import *


def longest_subsequence(head):
    if not head:
        return None

    prev = None
    node = head

    cnt = 0
    cnt_max = 0
    first_prev = prev
    last = head
    best_first_prev = prev
    best_last = head
    only_one_longest = True

    while node:
        if not prev or prev.val < node.val:
            cnt += 1
            last = node
        else:
            first_prev = prev
            last = node
            cnt = 1

        if cnt == cnt_max:
            only_one_longest = False

        if cnt > cnt_max:
            cnt_max = cnt
            best_first_prev = first_prev
            best_last = last
            only_one_longest = True

        prev = node
        node = node.next
    return cnt_max, best_first_prev, best_last, only_one_longest


def zad_21(head):
    cnt_max, best_first_prev, best_last, only_one_longest = longest_subsequence(head)

    if only_one_longest:
        if not best_first_prev:
            head = best_last.next
        else:
            best_first_prev.next = best_last.next

    return head






c1 = create_list([0,1,2,3,4,1,2])
max_cnt, best_first, best_last, only_one_longest = longest_subsequence(c1)
# print(max_cnt)
# print(best_first.val if best_first else None)
# print(best_last.val)
# print(only_one_longest)

print_all(zad_21(c1))
