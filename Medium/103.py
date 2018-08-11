# ------------------------------
# 103. Binary Tree Zigzag Level Order Traversal
# 
# Description:
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
# 
# Version: 1.0
# 08/10/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        stack = [root]
        res = []
        order = True # from left to right
        while stack:
            temp = []
            if order:
                res.append([node.val for node in stack])
            
            else:
                res.append([node.val for node in stack[::-1]])
            
            for node in stack:
                temp.extend([node.left, node.right])
                
            stack = [node for node in temp if node]
            order = not order
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Similar to problem 102.