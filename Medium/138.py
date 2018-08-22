# ------------------------------
# 138. Copy List with Random Pointer
# 
# Description:
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# Return a deep copy of the list.
# 
# Version: 1.0
# 08/21/18 by Jianfa
# ------------------------------

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        iterhead = head
        
        while iterhead:
            nextnode = iterhead.next
            
            copynode = RandomListNode(iterhead.label)
            iterhead.next = copynode
            copynode.next = nextnode
            
            iterhead = nextnode
        
        iterhead = head
        while iterhead:
            if iterhead.random:
                iterhead.next.random = iterhead.random.next
                
            iterhead = iterhead.next.next
        
        iterhead = head
        startpointer = RandomListNode(0)
        copyiter = startpointer
        
        while iterhead:
            nextnode = iterhead.next.next
            
            copynode = iterhead.next
            copyiter.next = copynode
            copyiter = copynode
            
            iterhead.next = nextnode
            
            iterhead = iterhead.next
        
        return startpointer.next
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from: https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)
# Key points:
# 1. Iterate the original list and duplicate each node. The duplicate of each node follows its original immediately.
# 2. Iterate the new list and assign the random pointer for each duplicated node.
# 3. Restore the original list and extract the duplicated nodes.