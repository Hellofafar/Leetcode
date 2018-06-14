# ------------------------------
# 226. Invert Binary Tree
# 
# Description:
# Invert a binary tree.
# Example:
# Input:
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 
# Output:
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# 
# Version: 1.0
# 06/12/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        
        if root.left:
            self.invertTree(root.left)
        
        if root.right:
            self.invertTree(root.right)
        
        if root.left or root.right:
            root.left, root.right = root.right, root.left
        
        return root

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Recursive solution. Invert the child from the left node, and finally invert child of root.