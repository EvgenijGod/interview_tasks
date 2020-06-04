"""
Given an integer k and a binary search tree, find the floor (less than or equal to) of k,
and the ceiling (larger than or equal to) of k.

If either does not exist, then print them as None.

"""


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    tmp = root_node
    while tmp:
        if tmp.value < k:
            floor = tmp.value
            tmp = tmp.right
        elif tmp.value > k:
            ceil = tmp.value
            tmp = tmp.left
        else:
            ceil = floor = k
            break
    return floor, ceil



if __name__ == "__main__":
    root = Node(8)
    root.left = Node(4)
    root.right = Node(12)

    root.left.left = Node(2)
    root.left.right = Node(6)

    root.right.left = Node(10)
    root.right.right = Node(14)

    print(findCeilingFloor(root, 5))
    # (4, 6)
