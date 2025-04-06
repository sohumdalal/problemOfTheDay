'''
Problem Of The Day - 4/7/2025:

Write a function that returns the number of leaf nodes in a binary tree (a node is a leaf if it has no children).

'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)
