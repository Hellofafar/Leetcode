# ------------------------------
# 138. Copy List with Random Pointer
# 
# Description:
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# Input:
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
# 
# Explanation:
# Node 1's value is 1, both of its next and random pointer points to Node 2.
# Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
# 
# Note:
# You must return the copy of the given head as a reference to the cloned list.
# 
# Version: 2.0
# 11/11/19 by Jianfa
# ------------------------------

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        prev = head
        while head:
            # interweave new nodes and old nodes just based on next pointers
            copyNode = Node(head.val, head.next, None)
            copyNode.next = head.next
            head.next = copyNode
            head = head.next.next
            
        copyPrev = prev.next
        head = prev
        while head:
            # build random connections
            if head.random is not None:
                head.next.random = head.random.next
            head = head.next.next
        
        head = prev
        copyHead = copyPrev
        while head:
            # divide the original node list and copied node list
            head.next = copyHead.next
            head = head.next
            
            if copyHead.next is not None:
                copyHead.next = copyHead.next.next
            copyHead = copyHead.next
        
        return copyPrev

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# More concise implementation.