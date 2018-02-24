# ------------------------------
# 543. Diameter of Binary Tree
# 
# Description:
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# 
# Example:
# Given a binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# Note: The length of path between two nodes is represented by the number of edges between them.
# 
# Version: 1.0
# 02/22/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = 1
        def findDepth(node):
            if not node:
                return 0
            L = findDepth(node.left)
            R = findDepth(node.right)
            self.depth = max(self.depth, (L + R + 1))
            return max(L, R) + 1
        
        findDepth(root)
        return self.depth - 1

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# The key point is findDepth function actually execute two action:
# 1) update self.depth.
# 2) return largest depth of this tree