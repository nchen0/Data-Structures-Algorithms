# 203. Remove Linked List Elements: https://leetcode.com/problems/remove-linked-list-elements/
"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return []
        original = ListNode(None)
        original.next = head
        head = original
        # We start out with a none node, instead of just start because we have to account for the 1st node being a value that needs to be deleted, along with further values being the same.
        while original.next:
            if original.next.val == val:
                original.next = original.next.next
            else:
                original = original.next

        return head.next
