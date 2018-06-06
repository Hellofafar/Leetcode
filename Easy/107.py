# ------------------------------
# 107. Binary Tree Level Order Traversal II
# 
# Description:
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
# 
# Version: 1.0
# 06/05/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        visited = []
        if not root:
            return res
        
        visited.append(root)
        while visited:
            sub_res = []
            for i in range(len(visited)):
                cur = visited.pop(0)
                if cur.left:
                    visited.append(cur.left)
                if cur.right:
                    visited.append(cur.right)
                
                sub_res.append(cur.val)
            
            res.insert(0, sub_res)
        
        return res


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# BFS solution. One of the smart point is use the length of current visited list to represent number of nodes in a level.