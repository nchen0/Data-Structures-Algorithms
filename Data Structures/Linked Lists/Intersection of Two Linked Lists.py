# 160. Intersection of Two Linked Lists: https://leetcode.com/problems/intersection-of-two-linked-lists/

"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        currentA = headA
        currentB = headB
        while currentA != currentB:
            # We're making two loops. Head A becomes head B if it's shorter, and if that happens it'll ensure that they end up at the same place, if intersecting.
            # If not intersecting, that second loop will make them end up at None at the same time, exit the loop, and we will return None for no intersection.
            currentA = headB if currentA is None else currentA.next
            currentB = headA if currentB is None else currentB.next
        return currentA
