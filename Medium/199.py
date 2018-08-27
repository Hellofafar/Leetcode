# ------------------------------
# 199. Binary Tree Right Side View
# 
# Description:
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# 
# Version: 1.0
# 08/26/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack = [root]
        res = []
        while stack:
            res.append(stack[-1].val)
            for _ in range(len(stack)):
                node = stack.pop(0)
                stack.append(node.left)
                stack.append(node.right)
            
            stack = [x for x in stack if x is not None]
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# BFS solution.