# ------------------------------
# 129. Sum Root to Leaf Numbers
# 
# Description:
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
        
        return self.helper(root, 0)
    
    def helper(self, root, num):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return num*10 + root.val
        
        return self.helper(root.left, num*10 + root.val) + self.helper(root.right, num*10 + root.val)
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Set two different ending condition:
# 1. root is null
# 2. root has no child