# ------------------------------
# 105. Construct Binary Tree from Preorder and Inorder Traversal
# 
# Description:
# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 
# Version: 2.0
# 11/11/19 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(in_l, in_r):
            nonlocal pre_idx
            # in_l is left bound of inorder range, in_r is right bound of inorder range
            if in_l == in_r:
                return None
            
            rootVal = preorder[pre_idx] # get current root value 
            root = TreeNode(rootVal)    # build the root TreeNode
            index = inorderDict[rootVal]
            
            pre_idx += 1                # Follow the order of preorder is actually DFS
            root.left = helper(in_l, index)    # recursively get left and right subtree
            root.right = helper(index+1, in_r)
            
            return root
        
        inorderDict = {val:i for i, val in enumerate(inorder)}
        pre_idx = 0
        return helper(0, len(inorder)) 

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Recursion solution from https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/
# Compare to 105.py, the better point is using index to denote what is the inorder range 
# of a tree, without sending a subarray as parameter.
# 
# O(N) time O(N) space
# 
# nonlocal: make a function inside a function, which uses the variable x (in the outer function) 
# as a non local variable 