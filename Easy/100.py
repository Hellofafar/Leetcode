# ------------------------------
# 100. Same Tree
# 
# Description:
# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes 
# have the same value.
# 
# Example 1:
# Input:     1         1
#           / \       / \
#          2   3     2   3
# 
#         [1,2,3],   [1,2,3]
# Output: true
# 
# Example 2:
# Input:     1         1
#           /           \
#          2             2
# 
#         [1,2],     [1,null,2]
# Output: false
# 
# Version: 1.0
# 05/25/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True

        elif not p and q:
            return False

        elif p and not q:
            return False

        elif p.val != q.val:
            return False

        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)