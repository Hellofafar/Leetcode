# ------------------------------
# 111. Minimum Depth of Binary Tree
# 
# Description:
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.
# Example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.
# 
# Version: 1.0
# 06/07/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        visited = [root]
        depth = 1
        while visited:
            for i in range(len(visited)):
                cur = visited.pop(0)
                if not cur.left and not cur.right:
                    return depth
                
                if cur.left:
                    visited.append(cur.left)
                
                if cur.right:
                    visited.append(cur.right)
            
            depth += 1
        
        return depth

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# BFS solution. Once a node with no child is found, return current depth.