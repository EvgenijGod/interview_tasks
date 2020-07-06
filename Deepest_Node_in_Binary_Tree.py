"""
You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

Example:

    a
   / \
  b   c
 /
d

The deepest node in this tree is d at depth 3.

"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


def deepest(node, n=1):
    if node is None:
        return None, -1
    if node.left is None and node.right is None:
        return node.val, n
    left = deepest(node.left, n + 1)
    right = deepest(node.right, n + 1)
    if left[1] > right[1]:
        return left
    return right


if __name__ == "__main__":
    root = Node('a')
    root.left = Node('b')
    root.left.left = Node('d')
    root.right = Node('c')

    print(deepest(root))
    # (d, 3)
