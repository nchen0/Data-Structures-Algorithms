# 234: Palindrome Linked List: https://leetcode.com/problems/palindrome-linked-list/


"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
"""


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        arr = []
        while current:
            arr.append(current.val)
            current = current.next
        print(arr)
        # Vs: arr[::-1]: Slicing creates a whole new list, copying every element from the original. reversed() just returns an iterator that walks the original list in reverse order, without copying anything.
        return arr == list(reversed(arr))
