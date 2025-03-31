'''
Problem Of The Day - 4/1/2025

Implement a Binary Search Tree (BST) with three traversal methods:

preorder(callback): Visit root → left → right

inorder(callback): Visit left → root → right

postorder(callback): Visit left → right → root

Instead of using one-liners, move the function calls to the next line for clarity.

Hint: Use recursion to traverse the tree and apply the callback function. Please refer to the boilerplate.


'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left:
                self._insert(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = TreeNode(val)

