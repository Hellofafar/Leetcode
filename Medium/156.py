# ------------------------------
# 156. Binary Tree Upside Down
# 
# Description:
# Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
# Example:
# Input: [1,2,3,4,5]
#     1
#    / \
#   2   3
#  / \
# 4   5
# 
# Output: return the root of the binary tree [4,5,2,#,#,3,1]
#    4
#   / \
#  5   2
#     / \
#    3   1
# 
# Version: 1.0
# 11/03/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left:  # If not root.left, there will be no root.right
            return root
        
        newRoot = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right  # This is important because it keeps "root" pointer
        root.left.right = root
        root.left = None
        root.right = None
        
        return newRoot
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# A recursive solution idea from https://leetcode.com/problems/binary-tree-upside-down/discuss/49406/Java-recursive-(O(logn)-space)-and-iterative-solutions-(O(1)-space)-with-explanation-and-figure