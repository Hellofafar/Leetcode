# ------------------------------
# 572. Subtree of Another Tree
# 
# Description:
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
# Example 1:
# Given tree s:
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4 
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# 
# Example 2:
# Given tree s:
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.
# 
# Version: 1.0
# 07/18/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.traverse(s, t)
    
    def traverse(self, s, t):
        return s != None and (self.equals(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t)) # Note that the last two conditions are traverse() not equals().
    
    def equals(self, s, t):
        if not s and not t:
            return True
        
        if not s or not t:
            return False
        
        return s.val == t.val and self.equals(s.left, t.left) and self.equals(s.right, t.right)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow solution: https://leetcode.com/problems/subtree-of-another-tree/solution/