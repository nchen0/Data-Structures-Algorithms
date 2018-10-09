# 141. Linked List Cycle: https://leetcode.com/problems/linked-list-cycle/description/
# Given a linked list, determine if it has a cycle in it.


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head:
            if head.val == "a":
                return True
            head.val = "a"
            head = head.next
        return False
