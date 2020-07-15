"""
You are given the preorder and inorder traversals of a binary tree in the form of arrays.
 Write a function that reconstructs the tree represented by these traversals.

Example:
Preorder: [a, b, d, e, c, f, g]
Inorder: [d, b, e, a, f, c, g]

The tree that should be constructed from these traversals is:

    a
   / \
  b   c
 / \ / \
d  e f  g
"""

from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''

        while len(q):
            n = q.popleft()
            result += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return result


def reconstruct(preorder, inorder, left=0, right=None):
    if right is None:
        right = len(preorder) - 1
        reconstruct.i = 0
    if left > right:
        return None

    elem = preorder[reconstruct.i]
    core_Node = Node(preorder[reconstruct.i])
    reconstruct.i += 1
    if left == right:
        return core_Node

    ind = inorder.index(elem)
    core_Node.left = reconstruct(preorder, inorder, left, ind - 1)
    core_Node.right = reconstruct(preorder, inorder, ind + 1, right)

    return core_Node


if __name__ == "__main__":
    tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
    print(tree)
    """
    abcdefg
        a
       / \
      b   c
     / \ / \
    d  e f  g
    """
