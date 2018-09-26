# ------------------------------
# 236. Lowest Common Ancestor of a Binary Tree
# 
# Description:
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
# 
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4
# 
# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of of nodes 5 and 1 is 3.
# 
# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
#              according to the LCA definition.
# 
# Note:
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.
# 
# Version: 1.0
# 09/26/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q):
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)    # Recursively to check the left subtree of root
        right = self.lowestCommonAncestor(root.right, p, q)  # Recursively to check the right subtree of root
        
        if left and right:  # If p and q are in left and right respectively, return root
            return root
        
        else:               # Else return either left or right
            return left or right

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65225/4-lines-C++JavaPythonRuby