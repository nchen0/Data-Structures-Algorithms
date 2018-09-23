# 700. Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/description/
# Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.


class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return []
        if root.val == val:
            return root
        else:
            if val < root.val:
                return self.searchBST(root.left, val)
            if val > root.val:
                return self.searchBST(root.right, val)
        return []
