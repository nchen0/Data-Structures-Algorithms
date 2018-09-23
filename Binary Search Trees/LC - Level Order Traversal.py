# 429. N-ary Tree Level Order Traversal
"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]
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
        answer = []
        while queue:
            size = len(queue)
            temp = []
            while size > 0:
                current = queue.pop(0)
                temp.append(current.val)
                for child in current.children:
                    queue.append(child)
                size -= 1
            answer.append(temp)
        return answer
