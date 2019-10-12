# ------------------------------
# 430. Flatten a Multilevel Doubly Linked List
# 
# Description:
# You are given a doubly linked list which in addition to the next and previous pointers, 
# it could have a child pointer, which may or may not point to a separate doubly linked 
# list. These child lists may have one or more children of their own, and so on, to produce 
# a multilevel data structure, as shown in the example below.
# 
# Flatten the list so that all the nodes appear in a single-level, doubly linked list. You 
# are given the head of the first level of the list.
# 
# Example:
# Input:
#  1---2---3---4---5---6--NULL
#          |
#          7---8---9---10--NULL
#              |
#              11--12--NULL
# Output:
# 1-2-3-7-8-11-12-9-10-4-5-6-NULL
# 
# Version: 1.0
# 10/11/19 by Jianfa
# ------------------------------

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        head, end = self.dfs(head)
        return head
        
    def dfs(self, head):
        start = head
        while start.next:
            if not start.child:
                start = start.next
        
            else:
                childStart, childEnd = self.dfs(start.child)
                childEnd.next = start.next
                start.next.prev = childEnd
                start.next = childStart
                childStart.prev = start
                start.child = None # Don't forget remove child
                start = childEnd.next
        
        if not start.child:
            # End of linked list
            return head, start
        
        else:
            childStart, childEnd = self.dfs(start.child)
            childEnd.next = start.next
            start.next = childStart
            childStart.prev = start
            start.child = None # Don't forget remove child
            start = childEnd
            return head, start

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DFS recursive solution