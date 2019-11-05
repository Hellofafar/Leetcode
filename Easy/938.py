# ------------------------------
# 938. Range Sum of BST
# 
# Description:
# Given the root node of a binary search tree, return the sum of values of all nodes 
# with value between L and R (inclusive).
# 
# The binary search tree is guaranteed to have unique values.
# 
# Example 1:
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
# 
# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23
#  
# Note:
# The number of nodes in the tree is at most 10000.
# The final answer is guaranteed to be less than 2^31.
# 
# Version: 1.0
# 11/04/19 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        
        return self.helper(root, L, R)
        
    def helper(self, root, L, R):
        if not root:
            return 0
        
        total = 0
        if root.val < L:
            # if root.val < L, only check its right child
            total += self.helper(root.right, L, R)
        elif root.val > R:
            # if root.val > R, only check its left child
            total += self.helper(root.left, L, R)
        else:
            # otherwise, normal inorder traversal
            total += self.helper(root.left, L, R)
            total += root.val
            total += self.helper(root.right, L, R)
            
        return total

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Inorder traversal solution.