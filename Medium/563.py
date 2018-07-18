# ------------------------------
# 563. Binary Tree Tilt
# 
# Description:
# Given a binary tree, return the tilt of the whole tree.
# The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.
# The tilt of the whole tree is defined as the sum of all nodes' tilt.
# Example:
# Input: 
#          1
#        /   \
#       2     3
# Output: 1
# Explanation: 
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1
# 
# Note:
# The sum of node values in any subtree won't exceed the range of 32-bit integer.
# All the tilt values won't exceed the range of 32-bit integer.
# 
# Version: 1.0
# 07/17/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.tilt = 0
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.helper(root)
        return self.tilt
        
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.tilt += abs(left - right)
        return left + right + root.val

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# The key point is to set a self.tilt value in the __init__ function as a global variable.
# Follow the idea from https://leetcode.com/problems/binary-tree-tilt/solution/