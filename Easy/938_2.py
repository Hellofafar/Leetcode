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
# Version: 2.0
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
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    # check left child
                    dfs(node.left)
                if R > node.val:
                    # check right child
                    dfs(node.right)
        
        self.ans = 0
        dfs(root)
        return self.ans

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DFS solution from https://leetcode.com/problems/range-sum-of-bst/solution/
# I also used inorder traversal to solve it.