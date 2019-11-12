# ------------------------------
# 106. Construct Binary Tree from Inorder and Postorder Traversal
# 
# Description:
# Given inorder and postorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_l, in_r):
            nonlocal post_idx
            if in_l == in_r:
                return None
            
            rootVal = postorder[post_idx] # get current root value
            root = TreeNode(rootVal)      # build the root node
            # root split inorder list into left and right subtree
            index = inorderDict[rootVal]
            
            post_idx -= 1
            # NOTE: do from right subtree first, because in postorder list
            # right node will be met first
            root.right = helper(index+1, in_r)
            root.left = helper(in_l, index)
            
            return root
        
        # build a hashmap for inorder {value:index}
        inorderDict = {val:i for i, val in enumerate(inorder)}
        post_idx = len(postorder) - 1
        return helper(0, len(inorder))

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Almost the same idea as 105_2, but do it from end to start, from right to left
# 
# O(N) time O(N) space