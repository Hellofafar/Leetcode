# ------------------------------
# 95. Unique Binary Search Trees II
# 
# Description:
# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
# Example:
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
# 
# Version: 1.0
# 08/08/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return []
        
        nums = [i for i in range(1, n+1)]
        return self.buildBST(nums)
        
    def buildBST(self, nums):
        if not nums:
            return [None]
        
        if len(nums) == 1:
            return [TreeNode(nums[0])]
        
        currlist = []
        for i in range(len(nums)):
            leftBST = self.buildBST(nums[:i])
            rightBST = self.buildBST(nums[i+1:])
            for j in range(len(leftBST)):  # Use nested for loop to build BST
                for k in range(len(rightBST)):
                    cur = TreeNode(nums[i])
                    cur.left = leftBST[j]
                    cur.right = rightBST[k]
                    currlist.append(cur)
        
        return currlist
            

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Dynamic programming solution.