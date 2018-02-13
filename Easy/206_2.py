# ------------------------------
# 206. Reverse Linked List
# 
# Description:
# Reverse a singly linked list.
# 
# Version: 1.0
# 02/06/18 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Revise the previous code by removing helper, since main function is same as helper function.