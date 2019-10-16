# ------------------------------
# 142. Linked List Cycle II
# 
# Description:
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# 
# Note: Do not modify the linked list.
# 
# Follow up:
# Can you solve it without using extra space?
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
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        
        p1 = head
        p2 = head
        hasCycle = False
        
        while p1 and p2:
            p1 = p1.next
            if not p2.next:
                return None
            p2 = p2.next.next
            if p1 == p2:
                hasCycle = True
                break
        
        if not hasCycle:
            return None
        
        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from https://leetcode.com/problems/linked-list-cycle-ii/discuss/44793/O(n)-solution-by-using-two-pointers-without-change-anything
# Have two pointers p1 and p2, p1 moves one step while p2 moves two steps each time.
# Assume two pointer first meet at step k
# cycle length is r
# 2k - k = nr  => k = nr
# Distance between start node of the list and start node of the cycle: s
# Distance between start node of the list and first meet node: k
# Distance between start node of the cycle and first meet node: m
# s = k - m
# s = nr - m = (n-1)r + (r - m)
# Let n = 1, using one pointer start from the start node of list, another pointer start from the first meeting node, 
# all of them wake one step at a time, the first time they meeting each other is the start of the cycle.