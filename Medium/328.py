# ------------------------------
# 328. Odd Even Linked List
# 
# Description:
# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
# 
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
# 
# Example 1:
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# 
# Example 2:
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
# 
# Note:
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...
# 
# Version: 1.0
# 09/27/19 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd = head
        even = head.next
        evenHead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenHead
        return head

# Used for testing
if __name__ == "__main__":
    test = Solution()
    head = []

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/odd-even-linked-list/solution/
# Main idea is using four pointer: head, odd, evenHead, even
# head and evenHead are head pointers of oddList and evenList, odd and even are tail pointers of oddList and evenList.
# Moving odd and even until the end and make odd.next = evenHead