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

    def preorder(self, callback):
        def traverse(node):
            if not node:
                return
            callback(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(self.root)

    def inorder(self, callback):
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            callback(node.val)
            traverse(node.right)
        traverse(self.root)

    def postorder(self, callback):
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            traverse(node.right)
            callback(node.val)
        traverse(self.root)

# Usage:
bst = BST()
for val in [5, 3, 8, 2, 4, 7, 9]:
    bst.insert(val)

print("Preorder:")
bst.preorder(print)

print("Inorder:")
bst.inorder(print)

print("Postorder:")
bst.postorder(print)
