# ------------------------------
# 203. Remove Linked List Elements
# 
# Description:
# Remove all elements from a linked list of integers that have value val.
# Example:
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# 
# Version: 1.0
# 06/07/18 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        zero = ListNode(0)
        pre = zero
        pre.next = head
        temp = head
        while head:
            if head.val == val:
                pre.next = head.next
                head = head.next
            
            else:
                pre = head
                head = head.next
        
        return zero.next
                

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 