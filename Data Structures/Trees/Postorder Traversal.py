# 145. Binary Tree Postorder Traversal: https://leetcode.com/problems/binary-tree-postorder-traversal/
# Postorder is left, right, then root.

"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
"""

# Recursive:


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        self.postRecursive(root, arr)
        return arr

    def postRecursive(self, root, arr):
        if root:
            self.postRecursive(root.left, arr)
            self.postRecursive(root.right, arr)
            arr.append(root.val)

# Iterative: Postorder is essentially almost preorder flipped, except instead of r->l->r, it should be r->right->left flipped, so we can change preorder's algorithm to append right into the array first, and flip the resulting array.


class Solution(object):
    def postorderTraversal(self, root):
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
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return arr[::-1]
