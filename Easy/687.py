# ------------------------------
# 687. Longest Univalue Path
# 
# Description:
# Given a binary tree, find the length of the longest path where each node in the path has the same value. 
# This path may or may not pass through the root.
# 
# Note: The length of path between two nodes is represented by the number of edges between them.
# 
# Example 1:
# Input:
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:
# 2
# 
# Input:
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output:
# 2
# 
# Version: 1.0
# 12/06/17 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        def length_path(node):
            if not node:
                return 0
            left_length = length_path(node.left)
            right_length = length_path(node.right)
            left_temp = right_temp = 0
            if node.left and node.val == node.left.val:
                left_temp = left_length + 1
            if node.right and node.val == node.right.val:
                right_temp = right_length + 1
            
            self.res = max(self.res, left_temp + right_temp)
            
            return max(left_temp, right_temp)
        
        length_path(root)
        return self.res
        
# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Recursive solution.