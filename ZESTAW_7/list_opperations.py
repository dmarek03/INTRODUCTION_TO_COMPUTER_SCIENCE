class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def append(head, val):
    new_node = Node(val)
    if head is None:
        return new_node

    node = head
    while node.next is not None:
        node = node.next

    node.next = new_node

    return head


def print_all(head):
    if head is None:
        print('Empty list')

    while head is not None:
        print(head.val)
        head = head.next


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


def create_list(list: list[int]):
    head = None
    for i in list:
        head = append(head, i)

    return head

