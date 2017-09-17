# ------------------------------
# 21. Merge Two Sorted Lists
# 
# Description:
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
# 
# Version: 1.0
# 09/17/17 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            if l1.val <= l2.val:
                mergedList = ListNode(l1.val)
                l1 = l1.next
            else:
                mergedList = ListNode(l2.val)
                l2 = l2.next
            
            currentNode = mergedList
            while l1 != None and l2 != None:
                if l1.val <= l2.val:
                    tempNode = ListNode(l1.val)
                    currentNode.next = tempNode
                    currentNode = currentNode.next
                    l1 = l1.next
                else:
                    tempNode = ListNode(l2.val)
                    currentNode.next = tempNode
                    currentNode = currentNode.next
                    l2 = l2.next
            
            if l1 == None:
                currentNode.next = l2
            else:
                currentNode.next = l1

            return mergedList


# ------------------------------
# Good idea from other solution:
# Java, 1 ms, using recursion: https://discuss.leetcode.com/topic/45002/java-1-ms-4-lines-codes-using-recursion
# if(l1 == null) return l2;
# if(l2 == null) return l1;
# if(l1.val < l2.val){
# 	l1.next = mergeTwoLists(l1.next, l2);
# 	return l1;
# } else{
# 	l2.next = mergeTwoLists(l1, l2.next);
# 	return l2;
# }