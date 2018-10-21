# 872. Leaf-Similar Trees - https://leetcode.com/problems/leaf-similar-trees/description/
"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

"""


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if (root1 is None and root2) or (root1 and root2 is None):
            return False

        def inner_leaf(root, array):
            if root.left:
                inner_leaf(root.left, array)
            if root.right:
                inner_leaf(root.right, array)
            if not root.left and not root.right:
                array.append(root.val)
        arr1 = []
        arr2 = []
        inner_leaf(root1, arr1)
        inner_leaf(root2, arr2)
        return arr1 == arr2
