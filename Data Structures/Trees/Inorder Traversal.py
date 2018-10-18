# 94. Binary Tree Inorder Traversal
# Inorder is left, root, then right.
"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
"""


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        self.recursive(root, arr)
        return arr

    def recursive(self, root, arr):
        if root:
            self.recursive(root.left, arr)
            arr.append(root.val)
            self.recursive(root.right, arr)
