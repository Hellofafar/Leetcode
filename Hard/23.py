# ------------------------------
# 25. Merge k Sorted Lists
# 
# Description:
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# 
# Version: 1.0
# 10/20/17 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import sys

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = current = ListNode(0)
        compare = []
        if not lists:
            return None
        
        for l in lists:
            if not l:
                compare.append(sys.maxsize)
            else:
                compare.append(l.val)
            
        while sys.maxsize not in compare or len(set(compare)) > 1:
            min_val = min(compare)
            min_list_idx = compare.index(min_val)
            current.next = ListNode(lists[min_list_idx].val)
            current = current.next
            
            lists[min_list_idx] = lists[min_list_idx].next
            if lists[min_list_idx]:
                compare[min_list_idx] = lists[min_list_idx].val
            else:
                compare[min_list_idx] = sys.maxsize
        
        return head.next
      

# Used for test
# [[], [-2], [-3,-2,-1]]

# ------------------------------
# Summary:
# Almost brute force.
# Better idea at: https://leetcode.com/problems/merge-k-sorted-lists/solution/
# Try to use Priority Queue