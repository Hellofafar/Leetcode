# ------------------------------
# 98. Validate Binary Search Tree
# 
# Description:
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# Example 1:
#     2
#    / \
#   1   3
# 
# Input: [2,1,3]
# Output: true
# 
# Example 2:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
# 
# Version: 2.0
# 11/11/19 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys

class Solution:
    last = -sys.maxsize
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        if not self.isValidBST(root.left):
            # check if left subtree is BST
            return False
        
        if root.val <= self.last:
            # check if current node is greater than last value
            return False
        else:
            self.last = root.val
        
        if not self.isValidBST(root.right):
            # check if right subtree is BST
            return False
        
        return True

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Inorder traverse solution with more concise implementation. Use a global variable last
# to store last node value.
# 
# O(N) time O(1) space