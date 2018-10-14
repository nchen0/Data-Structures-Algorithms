# A binary tree is any tree that has 2 child nodes from each parent. A binary search tree is an ordered binary tree where the parent node is always greater than the left child and less than the right child.

# Example of a Node on a binary tree:


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

    def __str__(self):
        return str(self.data)


# Here is a simple binary tree with 4 nodes:
"""
      tree
      ----
       1    <-- root
     /   \
    2     3  
   /   
  4
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
