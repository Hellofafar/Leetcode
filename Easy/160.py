# ------------------------------
# 160. Intersection of Two Linked Lists
# 
# Description:
# Write a program to find the node at which the intersection of two singly linked lists begins.
# For example, the following two linked lists:
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.
# 
# Notes:
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# 
# Version: 1.0
# 06/08/18 by Jianfa
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
        while a or b:
            if a:
                a = a.next
            else:
                headB = headB.next
                
            if b:
                b = b.next
            else:
                headA = headA.next
        
        while headA is not headB:
            headA = headA.next
            headB = headB.next
        
        return headA

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Two pointers solution.
# Another solution is hash table solution, which is to store every node in the dictionary and traverse two lists.
# If a node is found twice that it's the intersection point.