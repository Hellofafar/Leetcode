# ------------------------------
# 101. Symmetric Tree
# 
# Description:
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# 
# Version: 1.0
# 06/01/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        else:
            return self.isMirror(root.left, root.right)

        
    def isMirror(self, p, q):
        if not p and not q:
            return True
        
        if not p and q:
            return False
        
        if p and not q:
            return False
        
        if p.val != q.val:
            return False
        
        else:
            return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Take use of the idea from 100 (recursive solution)
# There is an iterative solution. The algorithm works similarly to BFS. Each time, two nodes are extracted and their 
# values compared. Then, the right and left children of the two nodes are inserted in the queue in opposite order. 