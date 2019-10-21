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
# 10/21/19 by Jianfa
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
            temp = head.next
            head.next = self.swapPairs(head.next.next)  # recursion
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
# Compare to 24.py, only change is temp = head.next