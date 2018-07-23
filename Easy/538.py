# ------------------------------
# 538. Convert BST to Greater Tree
# 
# Description:
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
# Example:
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13
# 
# Version: 1.0
# 07/14/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.pre = None
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        
        self.convertBST(root.right)
        
        if self.pre != None:
            root.val += self.pre
        
        self.pre = root.val
        
        self.convertBST(root.left)
        
        return root

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Very similar to problem 530. Use inorder traversal but start from the right to left.