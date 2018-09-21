# A Binary Search Tree is a type of Binary Tree where the left child node is smaller and the right child node is bigger than the root node.

# Binary Tree Implementation


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# insert: insert adds the input value to the binary search tree
    def insert(self, value):
        node = BinarySearchTree(value)
        if not self.value:
            self.value = node
        else:
            if value < self.value:
                self.left.insert(value)
            else:
                self.right.insert(value)


bst = BinarySearchTree(5)
