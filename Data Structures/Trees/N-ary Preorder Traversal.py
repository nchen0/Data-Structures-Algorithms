# 589. N-ary Tree Preorder Traversal - https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/
# Given an n-ary tree, return the preorder traversal of its nodes' values.


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # Iterative method:
        arr = []
        if not root:
            return arr
        stack = [root]
        while stack:
            current = stack.pop()
            arr.append(current.val)
            for child in current.children[::-1]:
                stack.append(child)
        return arr

# Recursive solution


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        arr = []
        if not root:
            return arr

        def recursion(root):
            arr.append(root.val)
            for child in root.children:
                recursion(child)
        recursion(root)
        return arr


# Alternative recursive solution, a bit faster:
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        arr = []
        self.recursion(root, arr)
        return arr

    def recursion(self, root, arr):
        if root is None:
            return arr
        arr.append(root.val)
        for child in root.children:
            self.recursion(child, arr)
