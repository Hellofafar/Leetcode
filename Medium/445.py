# ------------------------------
# 445. Add Two Numbers II
# 
# Description:
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit 
# comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
# 
# Example:
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# 
# Version: 1.0
# 10/06/17 by Jianfa
# ------------------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2= 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        
        sum_num = num1 + num2
        if sum_num == 0:
            return ListNode(0)
        head = None
        while sum_num:
            digit = sum_num % 10
            sum_num = sum_num // 10
            current = ListNode(digit)
            current.next = head
            head = current
        
        return head
             

# Used for test
if __name__ == "__main__":
    test = Solution()
    a1 = ListNode(7)
    a2 = ListNode(2)
    a3 = ListNode(4)
    a4 = ListNode(0)
    a1.next = a2
    a2.next = a3
    a3.next = a4

    b1 = ListNode(5)
    b2 = ListNode(6)
    b3 = ListNode(0)
    b1.next = b2
    b2.next = b3

    res = test.addTwoNumbers(a4, b3)
    while res:
        print(res.val)
        res = res.next

# ------------------------------
# Summary:
# O(m+n) solution.
# One border problem is when two numbers are 0, remember to think about output for it.
# Another idea from other's solution is to make num1 and num2 string that can generate result from head to tail.
# Since process from head, so that can let head = ListNode(0) at first, and don't have to decide if sum_num == 0.