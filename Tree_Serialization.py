"""
You are given the root of a binary tree. You need to implement 2 functions:

1. serialize(root) which serializes the tree into a string representation
2. deserialize(s) which deserializes the string back to the original tree that it represents
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # pre-order printing of the tree.
        result = ''
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result


def serialize(root):
    if root is not None:
        return str(root.val) + " " + serialize(root.left) + " " + serialize(root.right)
    return "#"


def deserialize(data):
    ind = -2

    def step():
        nonlocal ind
        ind += 2
        if ind >= len(data) or data[ind] == '#':
            return None
        node = Node(data[ind])
        node.left = step()
        node.right = step()
        return node

    return step()


if __name__ == "__main__":
    #     1
    #    / \
    #   3   4
    #  / \   \
    # 2   5   7
    tree = Node(1)
    tree.left = Node(3)
    tree.left.left = Node(2)
    tree.left.right = Node(5)
    tree.right = Node(4)
    tree.right.right = Node(7)

    print(serialize(tree))
    # 1 3 2 # # 5 # # 4 # 7 # #
    print(deserialize('1 3 2 # # 5 # # 4 # 7 # #'))
    # 132547
