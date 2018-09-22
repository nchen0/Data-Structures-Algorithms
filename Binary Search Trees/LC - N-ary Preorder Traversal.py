# 589. N-ary Tree Preorder Traversal
# Given an n-ary tree, return the preorder traversal of its nodes' values.


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        arr = []
        if not root:
            return arr
        queue = [root]
        while queue:
            current = queue.pop()
            arr.append(current.val)
            for child in current.children[::-1]:
                queue.append(child)
        return arr

        """Recursive method: 
        arr = []
        if not root:
            return arr 
        def recursion(root):
            arr.append(root.val)
            for child in root.children:
                recursion(child)
        recursion(root)
        return arr
        """
