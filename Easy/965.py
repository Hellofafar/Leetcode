# ------------------------------
# 965. Univalued Binary Tree
# 
# Description:
# A binary tree is univalued if every node in the tree has the same value.
# 
# Return true if and only if the given tree is univalued.
# 
# Example 1:
# Input: [1,1,1,1,1,null,1]
# Output: true
# 
# Example 2:
# Input: [2,2,2,5,2]
# Output: false
# 
# Note:
# 
# The number of nodes in the given tree will be in the range [1, 100].
# Each node's value will be an integer in the range [0, 99].
# 
# Version: 1.0
# 11/20/19 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        left = self.isUnivalTree(root.left) if root.left else True
        right = self.isUnivalTree(root.right) if root.right else True
        
        leftVal = root.left.val if root.left else root.val
        rightVal = root.right.val if root.right else root.val
        
        return left and right and root.val == leftVal == rightVal

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Recursive solution.
# 
# O(N) time O(H) space, H is the height of the given tree