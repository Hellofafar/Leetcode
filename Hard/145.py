# ------------------------------
# 145. Binary Tree Postorder Traversal
# 
# Description:
# Given a binary tree, return the postorder traversal of its nodes' values.
# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# Output: [3,2,1]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
# Version: 1.0
# 12/18/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)  # Use append rather than insert is because insert's complexity is O(n)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        return res[::-1]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Similar to problem 590.
# One thing to note is adding node to result list with append method rather than insert method,
# and return the reverse result list finally.
# If using insert(), complexity would be O(n^2)