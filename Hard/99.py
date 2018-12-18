# ------------------------------
# 99. Recover Binary Search Tree
# 
# Description:
# Two elements of a binary search tree (BST) are swapped by mistake.
# Recover the tree without changing its structure.
# 
# Example 1:
# Input: [1,3,null,null,2]
#    1
#   /
#  3
#   \
#    2
# 
# Output: [3,1,null,null,2]
#    3
#   /
#  1
#   \
#    2
# 
# Example 2:
# Input: [3,1,4,null,null,2]
#   3
#  / \
# 1   4
#    /
#   2
# 
# Output: [2,1,4,null,null,3]
#   2
#  / \
# 1   4
#    /
#   3
# 
# Follow up:
# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?
# 
# Version: 1.0
# 12/17/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys

class Solution:
    firstElement = None  # First element to swap
    secondElement = None  # Second element to swap
    preElement = TreeNode(-sys.maxsize)
    
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        temp = self.firstElement.val
        self.firstElement.val = self.secondElement.val
        self.secondElement.val = temp
        
    def traverse(self, root):
        if not root:
            return
        
        self.traverse(root.left)
        
        # Find the firstElement and secondElement
        if not self.firstElement and self.preElement.val > root.val:
            self.firstElement = self.preElement
        
        if self.firstElement and self.preElement.val > root.val:  # Notice the condition
            self.secondElement = root
        
        self.preElement = root

        self.traverse(root.right)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from https://leetcode.com/problems/recover-binary-search-tree/discuss/32535/No-Fancy-Algorithm-just-Simple-and-Powerful-In-Order-Traversal
# Key idea is using in-order traverse idea, find the first element which is larger than current node,
# and second element which is smaller than previous node.