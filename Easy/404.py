# ------------------------------
# 404. Sum of Left Leaves
# 
# Description:
# Find the sum of all left leaves in a given binary tree.
# Example:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
# 
# Version: 1.0
# 06/28/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        res = []
        self.helper(root, res, 1) # root node is not leave
        
        return sum(res)
        
    def helper(self, root, res, direction):
        if not root.left and not root.right:
            if direction == 0:
                res.append(root.val)
        
        if root.left:
            self.helper(root.left, res, 0)
        
        if root.right:
            self.helper(root.right, res, 1)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 