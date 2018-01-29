# ------------------------------
# 86. Partition List
# 
# Description:
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater 
# than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# 
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
# 
# Version: 1.0
# 01/28/18 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        start = ListNode(0)
        start.next = head
        pre = start
        anchor = False
        while head:
            print('head:', head.val)
            if head.val >= x:
                if not anchor:
                    partition = head
                    partition_pre = pre
                    anchor = True
                
                head = head.next
                pre = pre.next
                
            else:
                if anchor:
                    temp = ListNode(head.val)
                    partition_pre.next = temp
                    temp.next = partition
                    partition_pre = temp
                    head = head.next
                    pre.next = head
                
                else:
                    head = head.next
                    pre = pre.next

        return start.next

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# I struggled at the problem for a long time, but I didn't use a good way for it.
# My solution is very simple. Actually there is only one partition node, which is the first node that is greater
# than or equal to x. When it is found, just keep moving position of nodes less than that to it's previous one 
# node.
# The better solution would be to use two node lists, one is the list p1 for nodes that less than x, another 
# list p2 is for nodes that greater than or equal to x. Traverse the given node and build such two list, finally 
# connect them.