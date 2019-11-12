# ------------------------------
# Binary Tree Level Order Traversal
# 
# Description:
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from 
# left to right, level by level).
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# 
# Version: 2.0
# 11/11/19 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        # BFS
        res = []
        queue = [root]
        while queue:
            temp = []     # values of this level of nodes
            children = [] # next level of nodes
            for node in queue:
                temp.append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            
            res.append(temp[:]) # actually here can be res.append(temp), res will not change as temp changes
            queue = children[:] # here must be children[:] otherwise queue will change as children changes
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Similar BFS solution but use a little more spaces.
# On 102.py, using list.pop(0) actually takes O(n) time because it needs to remap the index
# of values. Use collections.deque instead.
# 
# O(N) time O(N) space