# ------------------------------
# 382. Linked List Random Node
# 
# Description:
# Given a singly linked list, return a random node's value from the linked list. Each node 
# must have the same probability of being chosen.
# 
# Follow up:
# What if the linked list is extremely large and its length is unknown to you? Could you 
# solve this efficiently without using extra space?
# 
# Example:
# // Init a singly linked list [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
# 
# // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
# solution.getRandom();
# 
# Version: 1.0
# 09/30/19 by Jianfa
# ------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        n = self.head
        ret = n.val
        i = 1
        while n.next:
            n = n.next
            if random.randint(0, i) == i:
                ret = n.val
            i += 1
        
        return ret

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from: https://leetcode.com/problems/linked-list-random-node/discuss/85662/Java-Solution-with-cases-explain
# Further introduction about Reservoir Sampling: https://leetcode.com/problems/linked-list-random-node/discuss/85659/Brief-explanation-for-Reservoir-Sampling
# and: https://gregable.com/2007/10/reservoir-sampling.html