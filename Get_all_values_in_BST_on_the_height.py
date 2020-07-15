"""
Given a binary tree, return all values given a certain height h.
"""


class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def valuesAtHeight(root, height):
    if root is None:
        return []
    if height == 1:
        return [root.value]
    return valuesAtHeight(root.left, height - 1) + valuesAtHeight(root.right, height - 1)


if __name__ == "__main__":
    #     1
    #    / \
    #   2   3
    #  / \   \
    # 4   5   7

    a = Node(1)
    a.left = Node(2)
    a.right = Node(3)
    a.left.left = Node(4)
    a.left.right = Node(5)
    a.right.right = Node(7)
    print(valuesAtHeight(a, 3))
    # [4, 5, 7]
