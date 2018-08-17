# ------------------------------
# 129. Sum Root to Leaf Numbers
# 
# Description:
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.
# Note: A leaf is a node with no children.
# Example:
# Input: [1,2,3]
#     1
#    / \
#   2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# 
# Example 2:
# Input: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
# 
# Version: 1.0
# 08/16/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return self.helper(root, "")
    
    def helper(self, root, numstr):
        if not root:
            return 0
        
        numstr = numstr + str(root.val)
        left = self.helper(root.left, numstr)
        right = self.helper(root.right, numstr)
        
        if not left and not right:
            try:
                num = int(numstr.lstrip('0'))  # If there are continuous '0', all will be removed.
            except:
                num = 0

            return num
        
        else:
            return left + right

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DFS solution.