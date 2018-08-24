# ------------------------------
# 143. Reorder List
# 
# Description:
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# You may not modify the values in the list's nodes, only nodes itself may be changed.
# 
# Example 1:
# Given 1->2->3->4, reorder it to 1->4->2->3.
# 
# Example 2:
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
# 
# Version: 1.0
# 08/23/18 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        p1 = head
        p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
            
        preMiddle = p1
        preCurrent = p1.next
        while preCurrent.next: # Reverse the node one by one
            current = preCurrent.next
            preCurrent.next = current.next
            current.next = preMiddle.next
            preMiddle.next = current
            
        p1 = head
        p2 = preMiddle.next
        while p1 != preMiddle:
            preMiddle.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = preMiddle.next
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow the idea from: https://leetcode.com/problems/reorder-list/discuss/44992/Java-solution-with-3-steps
# Reverse the second half of nodes at first.
# Then insert the nodes in second half to the first half of nodes one by one.