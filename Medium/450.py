# ------------------------------
# 450. Delete Node in a BST
# 
# Description:
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
# 
# Basically, the deletion can be divided into two stages:
# Search for a node to remove.
# If the node is found, delete the node.
# 
# Note: Time complexity should be O(height of tree).
# 
# Example:
# root = [5,3,6,2,4,null,7]
# key = 3
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# 
# Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
#     5
#    / \
#   4   6
#  /     \
# 2       7
# 
# Another valid answer is [5,2,6,null,4,null,7].
#     5
#    / \
#   2   6
#    \   \
#     4   7
# 
# Version: 1.0
# 12/21/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            if not root.left:  # If there is no left subtree, return right subtree directly
                root = root.right
            
            elif not root.right:  # If there is no right subtree, return left subtree directly
                root = root.left
            
            else:
                minNode = self.findMin(root.right)  # Find a minimum node at the right subtree and replace root with it
                root.val = minNode.val
                root.right = self.deleteNode(root.right, root.val)
        
        return root
    
    def findMin(self, root):
        while root.left:
            root = root.left
        
        return root

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from https://leetcode.com/problems/delete-node-in-a-bst/discuss/93296/Recursive-Easy-to-Understand-Java-Solution
# Steps:
# 
# Recursively find the node that has the same value as the key, while setting the left/right nodes equal to the returned subtree
# Once the node is found, have to handle the below 4 cases
# node doesn't have left or right - return null
# node only has left subtree- return the left subtree
# node only has right subtree- return the right subtree
# node has both left and right - find the minimum value in the right subtree, set that value to the currently found node, then recursively delete the minimum value in the right subtree