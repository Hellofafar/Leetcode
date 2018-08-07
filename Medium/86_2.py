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
# Version: 2.0
# 01/28/18 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
        l1 = ListNode(0)
        l2 = ListNode(0)
        head1 = l1
        head2 = l2
        while head:
            if head.val < x:
                head1.next = head
                head1 = head1.next
            else:
                head2.next = head
                head2 = head2.next
            
            head = head.next
        
        head2.next = None
        head1.next = l2.next
        return l1.next
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Two node lists solution. One is the list p1 for nodes that less than x, another list p2 is for nodes that 
# greater than or equal to x. Traverse the given node and build such two list, finally connect them.