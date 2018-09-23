# 590. N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/
# Given an n-ary tree, return the postorder traversal of its nodes' values.


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

        """Recursive method:
        arr = []
        if not root:
            return arr
        def recursive_postorder(root):
            for child in root.children:
                recursive_postorder(child)
            arr.append(root.val)
        recursive_postorder(root)
        return arr
        """
