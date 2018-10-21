# 590. N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/
# Given an n-ary tree, return the postorder traversal of its nodes' values.


# Iterative Solution
class Solution(object):
    def postorder(self, root):
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
            for child in current.children:
                stack.append(child)
        return arr[::-1]

# Recursive solution


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        arr = []
        self.recursion(root, arr)
        return arr

    def recursion(self, root, arr):
        if not root:
            return arr
        for child in root.children:
            self.recursion(child, arr)
        arr.append(root.val)
