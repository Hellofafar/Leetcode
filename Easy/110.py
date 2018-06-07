# ------------------------------
# 110. Balanced Binary Tree
# 
# Description:
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# 
# Example 2:
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.
# 
# Version: 1.0
# 06/06/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        height = self.helper(root)
        if height == -1:
            return False
        
        else:
            return True
        
    def helper(self, root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        else:
            left_height = self.helper(root.left)
            right_height = self.helper(root.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            
            else:
                return max(left_height, right_height) + 1

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DFS solution. Once difference of left height and right height is greater than 1, then tree height is -1.
# If left height or right height is -1, the tree height is -1 too.
# If root height is -1, then this tree is not balanced. 