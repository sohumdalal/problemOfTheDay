'''
Problem Of The Day - 4/3/2025

Given a BST and two node values, find the Lowest Common Ancestor (LCA) of the two nodes. The LCA is the deepest node that has both nodes as descendants.

Example:


        6
       / \
      2   8
     / \  / \
    0   4 7 9

LCA of 2 and 8 → 6
LCA of 2 and 4 → 2

Hint:

If both nodes are less than the root, search left.

If both nodes are greater than the root, search right.

Otherwise, the current node is the LCA.

'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lowest_common_ancestor(root, p, q):
    if not root:
        return None

    if p < root.val and q < root.val:
        return lowest_common_ancestor(root.left, p, q)

    if p > root.val and q > root.val:
        return lowest_common_ancestor(root.right, p, q)

    return root

# Example BST
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# Find LCA
lca_node = lowest_common_ancestor(root, 2, 8)
print("LCA of 2 and 8:", lca_node.val)  # Output: 6