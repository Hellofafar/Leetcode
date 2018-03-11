# ------------------------------
# 92. Reverse Linked List II
# 
# Description:
# Reverse a linked list from position m to n. Do it in-place and in one-pass.
# 
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# return 1->4->3->2->5->NULL.
# 
# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.
# 
# Version: 1.0
# 02/24/18 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m-1):
            pre = pre.next
            
        start = pre.next
        then = start.next
        
        for j in range(n - m):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next
            
        return dummy.next

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea is from https://leetcode.com/problems/reverse-linked-list-ii/discuss/30666/Simple-Java-solution-with-clear-explanation
# The key point is to set four pointer: dummy, pre, start, then
# dummy points to head, used to return in the end
# pre always point to the position where starts to reverse
# start points to the first node to be reversed
# then is the next point of start point
# First for loop get the pre pointer position, second for loop traverse the link one by one until the n postion.