# ------------------------------
# 105. Construct Binary Tree from Preorder and Inorder Traversal
# 
# Description:
# Given preorder and inorder traversal of a tree, construct the binary tree.
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# 
# Return the following binary tree:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 
# Version: 1.0
# 08/11/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        rootidx = inorder.index(preorder[0])
        left_pre = preorder[1:1+rootidx]
        left_in = inorder[:rootidx]
        right_pre = preorder[rootidx+1:]
        right_in = inorder[rootidx+1:]
        
        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)
        
        return root

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DFS recursive solution. Two order lists have different usage:
# 1. preorder: the first item is root node
# 2. inorder: find the root index, then the left side of root is left child tree of root,
# the right side of root is right child tree.
# 
# Recursively build tree.