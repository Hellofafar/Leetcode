# ------------------------------
# 24. Swap Nodes in Pairs
# 
# Description:
# Given a linked list, swap every two adjacent nodes and return its head.
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Your algorithm should use only constant space. You may not modify the 
# values in the list, only nodes itself can be changed.
# 
# Version: 1.0
# 09/20/17 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        elif head.next == None:
            return head
        else:
            temp = ListNode(head.next.val)
            head.next = self.swapPairs(head.next.next)
            temp.next = head
            head = temp
            return head
                

# Used for test
# if __name__ == "__main__":
#     test = Solution()
#     d = ListNode(2)
#     d.next = None
#     c = ListNode(1)
#     c.next = d
#     b = ListNode(4)
#     b.next = c
#     a = ListNode(3)
#     a.next = b
    
#     head = test.swapPairs(a)
#     while head != None:
#         print(head.val)
#         head = head.next

# ------------------------------
# Summary:
# At first I think only the second one is larger should be switched, but I misunderstood.
# It's a very typical recursion problem. I think about this because the return form is 
# similar to input variable's form.
# 
# 
# There is a similar situation but not use a temp variable.
# Reference: https://leetcode.com/problems/swap-nodes-in-pairs/discuss/
# def swapPairs(self, head):
#     pre, pre.next = self, head
#     while pre.next and pre.next.next:
#         a = pre.next
#         b = a.next
#         pre.next, b.next, a.next = b, a, b.next  # Can change three references at once
#         pre = a
#     return self.next