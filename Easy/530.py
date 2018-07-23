# ------------------------------
# 530. Minimum Absolute Difference in BST
# 
# Description:
# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
# Example:
# Input:
#    1
#     \
#      3
#     /
#    2
# Output:
# 1
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
# 
# Note: There are at least two nodes in this BST.
# 
# Version: 1.0
# 07/14/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def __init__(self):
        self.minDiff = float('inf')
        self.pre = None
    
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return self.minDiff
        
        self.getMinimumDifference(root.left)
        
        if self.pre != None:
            self.minDiff = min(self.minDiff, root.val - self.pre)
        
        self.pre = root.val
        
        self.getMinimumDifference(root.right)
        
        return self.minDiff

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Inorder travesal solution. Idea from https://leetcode.com/problems/minimum-absolute-difference-in-bst/discuss/99905/Two-Solutions-in-order-traversal-and-a-more-general-way-using-TreeSet