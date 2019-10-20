# ------------------------------
# 160. Intersection of Two Linked Lists
# 
# Description:
# 
# Version: 2.0
# 10/18/19 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        b = headB
        # we way iterate two times here
        # when any pointer reach the end, redirect it to another list
        # if two lists intersect exactly, after redirecting two pointers will reach the same node at the same time
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        
        return a

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Two pointers solution but more concise
# Idea from https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments