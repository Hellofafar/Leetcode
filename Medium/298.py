# ------------------------------
# 298. Binary Tree Longest Consecutive Sequence
# 
# Given a binary tree, find the length of the longest consecutive sequence path.
# 
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child 
# connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
# 
# For example,
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.
# 
# Version: 1.0
# 11/07/17 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(None, root, 0)
        
    def dfs(self, parent, current, length):
        if not current:
            return length
        
        if not parent or parent.val + 1 != current.val:
            length = 1
        else:
            length += 1
        
        return max(self.dfs(current, current.left, length), self.dfs(current, current.right, length), length)

# ------------------------------
# Summary:
# Top-Down DFS
# We use a variable length to store the current consecutive path length and pass it down the tree. As we traverse, 
# we compare the current node with its parent node to determine if it is consecutive. If not, we reset the length.