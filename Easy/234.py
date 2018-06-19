# ------------------------------
# 234. Palindrome Linked List
# 
# Description:
# Given a singly linked list, determine if it is a palindrome.
# Example 1:
# Input: 1->2
# Output: false
# 
# Example 2:
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
# Version: 1.0
# 06/18/18 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        slow = head
        fast = head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next
        
        node = None
        while slow.next:
            temp = slow.next
            slow.next = node
            node = slow
            slow = temp
        
        slow.next = node
        
        while head and slow:
            if head.val != slow.val:
                return False
            
            else:
                head = head.next
                slow = slow.next
        
        return True
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Reverse the second half of linked list and compare to the first half of list.