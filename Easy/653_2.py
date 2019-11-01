# ------------------------------
# 653. Two Sum IV - Input is a BST
# 
# Description:
# Given a Binary Search Tree and a target number, return true if there exist two elements 
# in the BST such that their sum is equal to the given target.
# 
# Example 1:
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# Target = 9
# Output: True
# 
# Example 2:
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# Target = 28
# Output: False
# 
# Version: 2.0
# 10/31/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = []
        self.inorder(root, nums)
        
        # Two pointers solution like Two Sum II
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                return True
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
        
        return False
    
    def inorder(self, root, nums):
        if not root:
            return
        
        self.inorder(root.left, nums)
        nums.append(root.val)
        self.inorder(root.right, nums)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Inorder traversal to get a sort array, then use two pointers like Two Sum II.
# Idea from: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/106059/JavaC%2B%2B-Three-simple-methods-choose-one-you-like
# 
# O(n) time, O(n) space