# ------------------------------
# 23. Merge k Sorted Lists
# 
# Description:
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# 
# Example:
# 
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# Version: 2.0
# 10/31/19 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        k = len(lists)
        nodeHeap = []
        for i in range(k):
            if lists[i]:
                # if lists[i] is not empty
                node = lists[i]
                heapq.heappush(nodeHeap, (node.val, i)) # (value, list_index)
        
        head = ListNode(0)
        start = head
        while len(nodeHeap) > 1:
            smallest = heapq.heappop(nodeHeap)
            index = smallest[1]
            
            curr = lists[index]
            start.next = curr
            start = start.next
            
            lists[index] = lists[index].next
            if lists[index] is not None:
                # if smallest.next is not none, push its next linkNode to the heap
                heapq.heappush(nodeHeap, (lists[index].val, index))
        
        if len(nodeHeap) == 1:
            # Only one linked list is left, append it to start directly
            last = heapq.heappop(nodeHeap)
            start.next = lists[last[1]]
        
        return head.next

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Heap solution. The element put in the heap is (val, list_index)
# 
# O(N*logk) k is the number of lists, N is nodes number. O(logk) for every pop and 
# insertion to heap
# O(N) for new linked list and O(k) for heap