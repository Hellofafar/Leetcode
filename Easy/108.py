# ------------------------------
# 108. Convert Sorted Array to Binary Search Tree
# 
# Description:
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# Example:
# Given the sorted array: [-10,-3,0,5,9],
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
# 
# Version: 1.0
# 06/05/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        head = self.helper(nums, 0, len(nums) - 1)
        
        return head
        
    def helper(self, nums, low, high):
        if low > high:
            return None
        
        mid = (low + high) / 2
        head = TreeNode(nums[mid])
        head.left = self.helper(nums, low, mid - 1)
        head.right = self.helper(nums, mid + 1, high)
        
        return head
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# I didn't pass at the first time because I ignored the condition "Binary Search Tree"