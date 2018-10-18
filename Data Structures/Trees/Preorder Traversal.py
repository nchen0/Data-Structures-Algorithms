# 144. Binary Tree Preorder Traversal: https://leetcode.com/problems/binary-tree-preorder-traversal/
# Preorder is from root to left to right.

"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive solution:


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        if not root:
            return arr
        self.recursive(root, arr)
        return arr

    def recursive(self, root, arr):
        arr.append(root.val)
        if root.left:
            self.recursive(root.left, arr)
        if root.right:
            self.recursive(root.right, arr)
# Iterative solution:


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        if not root:
            return arr
        stack = [root]
        while stack:
            current = stack.pop()
            arr.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return arr
