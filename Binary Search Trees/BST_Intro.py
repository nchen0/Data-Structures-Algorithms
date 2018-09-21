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
        if not self:
            self = node
        # To prevent against duplicates.
        if self.value == node.value:
            return
        else:
            if value < self.value:
                if not self.left:
                    self.left = node
                else:
                    self.left.insert(value)
            if value > self.value:
                if not self.right:
                    self.right = node
                else:
                    self.right.insert(value)

# search: If target is in the tree, return True, else return False
    def search(self, target):
        if self.value == target:
            return True
        else:
            if target < self.value:
                return self.left.search(target)
            if target > self.value:
                return self.right.search(target)
        return False


# insert out of class: (node is already a node, not a value).
def insert(root, node):
    # Code here
    if not root:
        root = node
    if root.value == node.value:
        return
    else:
        if node.value < root.value:
            if not root.left:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if not root.right:
                root.right = node
            else:
                insert(root.right, node)

# insertion with Node & BinarySearchTree Class:


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)
        # Enter you code here.

    def _insert(self, val, node):
        if val < node.info:
            if node.left == None:
                node.left = Node(val)
            else:
                self._insert(val, node.left)
        elif val > node.info:
            if node.right == None:
                node.right = Node(val)
            else:
                self._insert(val, node.right)

        else:
            print("value already in tree")

# deletion
