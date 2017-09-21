# ------------------------------
# 25. Reverse Nodes in k-Group
# 
# Description:
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# 
# You may not alter the values in the nodes, only nodes itself may be changed.
# Only constant memory is allowed.
# For example,
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5
# 
# Version: 1.0
# 09/21/17 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pointer = {}
        if not head:
            return None
        else:
            i = 0
            temp = head
            while temp and i < k:
                pointer[i] = temp
                temp = temp.next
                i += 1
            
            if i < k:
                return head
            else:
                while i > 1:
                    pointer[i-1].next = pointer[i-2]
                    i -= 1
                pointer[0].next = self.reverseKGroup(temp, k)
                return pointer[k-1]
      

# Used for test
# if __name__ == "__main__":
#     test = Solution()
#     d = ListNode(2)
#     d.next = None
#     c = ListNode(1)
#     c.next = d
#     b = ListNode(4)
#     b.next = c
#     a = ListNode(3)
#     a.next = b
    
#     head = test.reverseKGroup(a, 3)
#     while head != None:
#         print(head.val)
#         head = head.next

# ------------------------------
# Summary:
# Still using recursion solution
# Some ideas from other solutions are processing every k nodes every time, until there are 
# no k nodes in the list.