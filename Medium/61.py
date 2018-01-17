# ------------------------------
# 61. Rotate List
# 
# Description:
# Given a list, rotate the list to the right by k places, where k is non-negative.
# Example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
# 
# Version: 1.0
# 01/15/18 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head
        
        dict_node = {}
        start = 0
        while head:
            dict_node[start] = head
            start += 1
            head = head.next
        
        if k >= start:
            k = k % start
        
        if k == 0:
            return dict_node[0]
        dict_node[start-k-1].next = None
        dict_node[start-1].next = dict_node[0]
        return dict_node[start-k]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Use a dictionary to store every node in the list at first.
# There are three situation for k:
# 1. k = 0, just no change
# 2. k less than list length n, then the (n-k+1)th node will be the head node when return. Make
# some change to node pointing relation.
# 3. k greater than or equal to length n, k = k % n, then come back to situation 1 or 2.