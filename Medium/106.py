# ------------------------------
# 106. Construct Binary Tree from Inorder and Postorder Traversal
# 
# Description:
# Given inorder and postorder traversal of a tree, construct the binary tree.
# Note:
# You may assume that duplicates do not exist in the tree.
# For example, given
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        rootidx = inorder.index(postorder[-1])
        left_in = inorder[:rootidx]
        left_post = postorder[:rootidx]
        right_in = inorder[rootidx+1:]
        right_post = postorder[rootidx:-1]
        
        root.left = self.buildTree(left_in, left_post)
        root.right = self.buildTree(right_in, right_post)
        
        return root


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Similar to problem 105, but mind the left and right are changed.