"""
- Formally, we define a tree T as a set of nodes storing elements such that the nodes have a parent-child relationship that satisfies the following properties:
    - If T is nonempty, it has a special node, called the root of T, that has no parent.
    - Each node v of T different from the root has a unique parent node w; every node with parent w is a child of w.
    - Two nodes that are children of the same parent are siblings. 
    - A node v is known as leaf if it has no children. 
    - A tree is ordered if there is a meaningful linear order among the children of each node. 
    - File systems, organizational hierarchies in a company are perfect uses of trees. 
    - There's tons of trees in CS: trees, binary trees, BST's, heaps, AVL's, Red & Black trees. 
    - Trees are powerful because they're dynamic data structures, easy to add or remove, like linked lists. Their structure conveys information. The fact that child/parent releationships exist tells us a lot.
    - Heap - root is most important
    - Huffman Tree - organized by character frequency
    - Search Trees - organized by node ordering
- A binary tree is any tree that has 2 child nodes from each parent.
- A binary search tree is an ordered binary tree where the parent node is always greater than the left child and less than the right child.
- A binary tree is an ordered tree with the following properties:
    - Every node has AT MOST, 2 children.
    - Each child node is laeled as either a left child or a right child.
    - A left child preceds a right child in the order of children of a node. 
- A binary tree is proper, or full, if every node has either 0 or 2 children. In a proper binary tree, every internal node has exactly two children. 
- A use of binary trees can arise from where we wish to convey yes or no questions/scenarios. Such trees are known as decision trees. 
- Binary trees have interestig properties dealing with relationships between their height and number of nodes. 
    - In a binary tree, level 0 has at most 1 node, 1 has at most 2 nodes, 2 has at most 4 nodes, 3 has at most 8 nodes, and so forth. 
"""
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
