# ------------------------------
# 876. Middle of the Linked List
# 
# Description:
# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# 
# If there are two middle nodes, return the second middle node.
# 
# Example 1:
# 
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# 
# Example 2:

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one. 
# 
# Note:
# The number of nodes in the given list will be between 1 and 100.
# 
# Version: 1.0
# 11/04/19 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head # fast pointer moves two nodes ahead each time
        slow = head # slow pointer moves one node ahead each time
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next: # have to check here because fast.next may be null here
                fast = fast.next
            else:
                # if there are even number of nodes
                return slow
        # if there are odd number of nodes
        return slow

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Two pointers solution.
# 
# O(N) time O(1) space