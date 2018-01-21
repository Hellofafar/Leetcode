# ------------------------------
# 83. Remove Duplicates from Sorted List
# 
# Description:
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# 
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
# 
# Version: 1.0
# 01/20/18 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next == None:
            return head
        
        temp = ListNode(0)
        temp.next = head

        while head.next:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        
        return temp.next

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Use a pre node (temp). Keep move head node until there is no next node. Return temp.next.