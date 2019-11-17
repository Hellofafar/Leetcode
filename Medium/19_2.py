# ------------------------------
# 19. Remove Nth Node From End of List
# 
# Description:
# Given a linked list, remove the n-th node from the end of list and return its head.
# 
# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# 
# Note:
# Given n will always be valid.
# 
# Follow up:
# Could you do this in one pass?
# 
# Version: 2.0
# 11/16/19 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = head
        
        p1 = head
        i = 0
        while i < n:
            p1 = p1.next
            i += 1
        
        if not p1:
            # if p1 is None, then means head is the nth node from end
            return head.next
        else:
            # else, move p2 with p1, until p1 reach None, p2 is the nth node from end
            last = None
            p2 = head
            while p1:
                last = p2
                p1 = p1.next
                p2 = p2.next
            last.next = p2.next
            return prev

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Two pointers solution. p1 move n step at first, if it's None, head is the nth node from end.
# Otherwise, move p2 from head together with p1, when p1 reach end p2 is the node to remove. 