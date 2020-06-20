"""
You are given two singly linked lists. The lists intersect at some node.
Find, and return the node. Note: the lists are non-cyclical.
"""


def intersection(a, b):  # O(n + m) time, O(n) memory
    s = set()
    while a is not None:
        s.add(a.val)
        a = a.next
    while b is not None:
        if b.val in s:
            return b
        b = b.next
    return b


def intersection2(a, b):  # O(n + m) time, O(1) memory
    a1 = a
    b1 = b
    a_cnt = 0
    b_cnt = 0
    while a_cnt != 2 and b_cnt != 2:
        if a1.val == b1.val:
            return a1
        a1 = a1.next
        b1 = b1.next
        if a1 is None:
            a_cnt += 1
            a1 = b
        if b1 is None:
            b_cnt += 1
            b1 = a
    return None


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def prettyPrint(self):
        c = self
        while c:
            print(c.val)
            c = c.next


if __name__ == "__main__":
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)

    b = Node(6)
    b.next = a.next.next

    c = intersection2(a, b)
    c.prettyPrint()
    # 3 4
