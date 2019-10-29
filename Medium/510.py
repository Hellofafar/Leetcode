# ------------------------------
# 510. Inorder Successor in BST II
# 
# Description:
# Given a binary search tree and a node in it, find the in-order successor of that 
# node in the BST.
# 
# The successor of a node p is the node with the smallest key greater than p.val.
# 
# You will have direct access to the node but not to the root of the tree. Each node 
# will have a reference to its parent node.
# 
# Note:
# If the given node has no in-order successor in the tree, return null.
# It's guaranteed that the values of the tree are unique.
# Remember that we are using the Node type instead of TreeNode type so their string 
# representation are different.
# 
# Version: 1.0
# 10/28/19 by Jianfa
# ------------------------------

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # the successor is somewhere lower in the right subtree
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        # the successor is somewhere upper in the tree
        while node.parent and node.val > node.parent.val:
            node = node.parent
        return node.parent

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Iterative solution from https://leetcode.com/problems/inorder-successor-in-bst-ii/solution/
# 1. If the node has a right child, and hence its successor is somewhere lower in the tree. 
# Go to the right once and then as many times to the left as you could. Return the node 
# you end up with.
# 
# 2. Node has no right child, and hence its successor is somewhere upper in the tree. Go up 
# till the node that is left child of its parent. The answer is the parent.
# 
# O(H) time, where H is the height of the tree. O(logN) in the average case, and O(N) in 
# the worst case, where N is the number of nodes in the tree.
# O(1) space