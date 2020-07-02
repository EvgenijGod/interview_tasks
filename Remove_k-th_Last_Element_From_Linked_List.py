"""
You are given a singly linked list and an integer k. Return the linked list,
removing the k-th last element from the list.

Try to do it in a single pass and using constant space.
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)


def remove_kth_from_linked_list(real_head, k):
    head = Node(0, real_head)
    i = 0
    ptr = head
    tmp = head
    while i <= k:
        ptr = ptr.next
        i += 1
    #print(ptr.val)
    while ptr is not None:
        ptr = ptr.next
        tmp = tmp.next
    elem = tmp.next
    tmp.next = elem.next
    del tmp
    real_head = head.next
    del head
    return real_head


if __name__ == "__main__":
    head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    print(head)
    # [1, 2, 3, 4, 5, 6]
    head = remove_kth_from_linked_list(head, 3)
    print(head)
    # [1, 2, 3, 5, 6]

