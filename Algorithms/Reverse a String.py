# 344. Reverse String: https://leetcode.com/problems/reverse-string/description/

"""
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s = []
        for i in range(len(s)-1, -1, -1):
            new_s.append(s[i])
        return ''.join(new_s)

# return s[::-1] is the easier way
