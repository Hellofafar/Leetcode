# ------------------------------
# 426. Convert Binary Search Tree to Sorted Doubly Linked List
# 
# Description:
# Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right 
# pointers as synonymous to the previous and next pointers in a doubly-linked list.
# 
# Version: 1.0
# 10/31/19 by Jianfa
# ------------------------------

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    prev = None
    
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        head = Node(0, None, None)
        self.prev = head
        self.helper(root)
        # connect the head and tail
        self.prev.right = head.right
        head.right.left = self.prev
        
        return head.right
    
    def helper(self, root):
        # in-order traversal and move prev node with adding left pointer and right pointer
        if not root:
            return
        
        self.helper(root.left)
        self.prev.right = root
        root.left = self.prev
        self.prev = root
        self.helper(root.right)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# In-order traversal idea from: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/discuss/149151/Concise-Java-solution-Beats-100
# step1: inorder tranversal by recursion to connect the original BST
# step2: connect the head and tail to make it circular
# Tips: Using head node to handle corner case