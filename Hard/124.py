# ------------------------------
# 124. Binary Tree Maximum Path Sum
# 
# Description:
# Given a non-empty binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
# 
# Example 1:
# Input: [1,2,3]
#        1
#       / \
#      2   3
# Output: 6
# 
# Example 2:
# Input: [-10,9,20,null,null,15,7]
#    -10
#    / \
#   9  20
#     /  \
#    15   7
# Output: 42
# 
# Version: 1.0
# 12/18/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys

class Solution:
    maxSum = 0
    maxNode = -sys.maxsize  # In case the largest path sum equal to some node, then return the largest node
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        
        return self.maxSum if self.maxSum != 0 else self.maxNode
    
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        self.maxNode = max(self.maxNode, root.val)
        
        self.maxSum = max(self.maxSum, root.val + left + right)
        
        maxSideSum = max(root.val + left, root.val + right)  # Max sum of a single side starting from root node
        
        return maxSideSum if maxSideSum > 0 else 0  # Return value will not be less than 0

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Similar idea from problem 543.
# 1. Calculate left and right max sum
# 2. Update maximum sum when path sum including current node is larger
# 3. Return largest path sum starting from current node