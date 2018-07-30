# ------------------------------
# 653. Two Sum IV - Input is a BST
# 
# Description:
# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
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
# Version: 1.0
# 07/29/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nodeset = set()
        return self.helper(root, k, nodeset)
    
    def helper(self, root, k, nodeset):
        if not root:
            return False
        
        if k - root.val in nodeset:
            return True
        
        nodeset.add(root.val)
        return self.helper(root.left, k, nodeset) or self.helper(root.right, k, nodeset)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Hashset solution.