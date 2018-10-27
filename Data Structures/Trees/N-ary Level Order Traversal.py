# 429. N-ary Tree Level Order Traversal: https://leetcode.com/problems/n-ary-tree-level-order-traversal/


"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        arr = []
        if not root:
            return arr
        queue = [root]
        while queue:
            count = len(queue)
            temp = []
            for _ in range(count):
                current = queue.pop(0)
                for child in current.children:
                    queue.append(child)
                temp.append(current.val)
            arr.append(temp)
        return arr
