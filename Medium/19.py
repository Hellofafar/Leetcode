# ------------------------------
# 19. Remove Nth Node From End of List
# 
# Description:
# Given a linked list, remove the nth node from the end of list and return its head.
# 
# For example,
#  Given linked list: 1->2->3->4->5, and n = 2.
# 
#  After removing the second node from the end, the linked list becomes 1->2->3->5.
# 
# Note:
# Given n will always be valid.
# Try to do this in one pass.
# 
# Version: 1.0
# 10/18/17 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        dict_Node = {}
        while head:
            dict_Node[count] = head
            count += 1
            head = head.next
        
        target = count - n
        if target - 1 in dict_Node and target + 1 in dict_Node:
            dict_Node[target - 1].next = dict_Node[target + 1]
            return dict_Node[0]
        elif target - 1 not in dict_Node and target + 1 in dict_Node:
            return dict_Node[target + 1]
        elif target - 1 in dict_Node and target + 1 not in dict_Node:
            dict_Node[target - 1].next = None
            return dict_Node[0]
        else:
            return None
    


# Summary
# I use a dictionary to store every node during counting, and remove the target one.
# Need to think over some boundary condition, for example the first Node or the last Node.
# 
# Get a good idea from the shortest-time solution:
# Use two pointer p1 and p2. Start from head, move p1 n steps. If p1 == None, then head is the target to be
# removed. If p1 is not None, then move p1 and p2 together until p1 reach None. Then p2.next is the target 
# to be removed. This idea is very smart!