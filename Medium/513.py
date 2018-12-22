# ------------------------------
# 513. Find Bottom Left Tree Value
# 
# Description:
# Given a binary tree, find the leftmost value in the last row of the tree.
# Example 1:
# Input:
#     2
#    / \
#   1   3
# Output:
# 1
# 
# Example 2: 
# Input:
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
# Output:
# 7
# 
# Note: You may assume the tree (i.e., the given root node) is not NULL.
# 
# Version: 1.0
# 12/21/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = [root]
        
        while nodes:
            children = []
            for i in range(len(nodes)):
                node = nodes.pop(0)
                if i == 0:  # leftmost value at current row
                    candidate = node.val
                
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            
            nodes = children
        
        return candidate
            

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# BFS solution