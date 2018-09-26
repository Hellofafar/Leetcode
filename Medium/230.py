# ------------------------------
# 230. Kth Smallest Element in a BST
# 
# Description:
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
# 
# Example 1:
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# 
# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# 
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
# 
# Version: 1.0
# 09/26/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        
        Inorder DFS, build the orderList one by one with inorder traverse.
        """
        orderList = []
        self.helper(root, orderList)
        return orderList[k-1]
    
    def helper(self, root, orderList):
        if not root:
            return
        
        self.helper(root.left, orderList)
        orderList.append(root.val)
        self.helper(root.right, orderList)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63660/3-ways-implemented-in-JAVA-(Python):-Binary-Search-in-order-iterative-and-recursive