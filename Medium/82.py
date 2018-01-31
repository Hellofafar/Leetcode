# ------------------------------
# 82. Remove Duplicates from Sorted List II
# 
# Description:
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# 
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
# 
# Version: 1.0
# 01/30/18 by Jianfa
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
        if not head or not head.next:
            return head
        
        start = ListNode(head.val - 1)
        start.next = head
        
        pre0 = start
        pre1 = head
        head = head.next
        duplicate = False
        while head:
            if head.val == pre1.val:
                duplicate = True
                head = head.next
                pre1.next = head
            elif duplicate:
                duplicate = False
                pre1 = head
                pre0.next = pre1
                head = head.next
            else:
                head = head.next
                pre1 = pre1.next
                pre0 = pre0.next
        
        if duplicate:
            pre0.next = head
            
        return start.next

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Use two former pointers, one for the first node of duplicate nodes (if existing), another one for the rest of
# duplicate nodes. A bool flag is used to record the duplicate status.
# When a duplicate value is detected, remove the following nodes one by one and delete the first node when a node 
# with new value is found.