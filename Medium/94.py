# ------------------------------
# 94. Binary Tree Inorder Traversal
# 
# Description:
# Given a binary tree, return the inorder traversal of its nodes' values.
# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
# Version: 1.0
# 08/07/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 