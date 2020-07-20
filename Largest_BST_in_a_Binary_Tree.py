"""
You are given the root of a binary tree.
Find and return the largest subtree of that tree, which is a valid binary search tree.
"""


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        # preorder traversal
        answer = str(self.key)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer


def largest_bst_subtree(root, minn=-1e100, maxx=1e100):
    if root is None:
        return None
    if root.key < minn or root.key > maxx:
        return None
    if root.left is None and root.right is None:
        return root
    left = largest_bst_subtree(root.left, minn, root.key)
    right = largest_bst_subtree(root.right, root.key, maxx)
    if left is None and right is not None:
        return right
    if left is not None and right is None:
        return left
    if left is None and right is None:
        return None
    return root



if __name__ == "__main__":
    #     5
    #    / \
    #   6   7
    #  /   / \
    # 2   6   9
    node = TreeNode(5)
    node.left = TreeNode(6)
    node.right = TreeNode(7)
    node.left.left = TreeNode(2)
    node.right.left = TreeNode(6)
    node.right.right = TreeNode(9)
    print(largest_bst_subtree(node))
    # 769
