# 637. Average of Levels in Binary Tree: https://leetcode.com/problems/average-of-levels-in-binary-tree/

"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
"""


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        arr = []
        queue = [root]
        while queue:
            # We keep a record of how long the queue array is so we can see how many nodes we need to take out & add.
            length = len(queue)
            sum = 0
            for _ in range(length):  # Iterate through each node in the queue.
                node = queue.pop(0)
                sum += node.val
                if node.left:  # If has left child, we want to add it to the queue so we can go through another layer.
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Once we go through a level, we add the average to the array
            arr.append(float(sum) / length)
        # At some point, there won't be a node.left, and node.right to add to the queue since we'll hit the leaves, at which point the while loop will terminate.
        return arr
