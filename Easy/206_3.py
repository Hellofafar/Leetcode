# ------------------------------
# 206. Reverse Linked List
# 
# Description:
# Reverse a singly linked list.
# 
# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# Follow up:
# A linked list can be reversed either iteratively or recursively. Could you implement both?
# 
# Version: 3.0
# 11/10/19 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        last = None
        while cur is not None:
            temp = cur.next
            cur.next = last
            last = cur
            cur = temp
        
        return last
            

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Iterative solution: reverse from begining.
# 
# O(N) time O(1) space 