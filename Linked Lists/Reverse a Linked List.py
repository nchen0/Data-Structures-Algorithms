# 206. Reverse Linked List: https://leetcode.com/problems/reverse-linked-list/description/
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""
# Iterative solution.


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Traverse through the linked list.
        while current:

            # Set a pointer to the current node's next node.
            next = current.next

            # We are turning every pointer around to reverse, so current's next pointer should be pointing to the prev node we initialized earlier. This also works as the beginning becomes the end, which is None.
            current.next = prev

            # We are done reversing this current node, so now we're setting up the prev to be the current node so that the next node we move to can point it's current.next to prev.
            prev = current

            # Moving on to the next node, which is the next that we initialized earlier to be able to move through the linked list.
            current = next

        # We are returning prev because prev is the "tail" of the original list, but is now the head because we reversed it.
        return prev

# Recursive solution.


class Solution:
    def reverse(head):
        return self.reverseList(head)

    def reverseList(self, node, prev=None):
        if node == None:
            # return the previous node when the control reaches the end of the recursion traversal
            # as the prev is supposed to have the starting reference to the reversed list
            return prev
        nextNode = node.next
        node.next = prev
        return self.reverseList(nextNode, node)
