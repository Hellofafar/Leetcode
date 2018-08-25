# ------------------------------
# 148. Sort List
# 
# Description:
# Sort a linked list in O(n log n) time using constant space complexity.
# Example 1:
# Input: 4->2->1->3
# Output: 1->2->3->4
# 
# Example 2:
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# 
# Version: 1.0
# 08/24/18 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        fast = head
        slow = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        
        h1 = self.sortList(head)
        h2 = self.sortList(slow)
        
        return self.merge(h1, h2)
    
    def merge(self, h1, h2):
        l = ListNode(0)
        p = l
        
        while h1 and h2:
            if h1.val < h2.val:
                l.next = h1
                h1 = h1.next
            else:
                l.next = h2
                h2 = h2.next
            
            l = l.next
        
        if h1:
            l.next = h1
        if h2:
            l.next = h2
        
        return p.next
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Merge sort solution from: https://leetcode.com/problems/sort-list/discuss/46714/Java-merge-sort-solution