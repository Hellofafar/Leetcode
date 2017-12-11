# ------------------------------
# 173. Binary Search Tree Iterator
# 
# Description:
# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node 
# of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of 
# the tree.
# 
# Version: 1.0
# 12/10/17 by Jianfa
# ------------------------------

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.nodeList = []
        curr = root
        while curr:
            self.nodeList.append(curr)
            curr = curr.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.nodeList else False
        

    def next(self):
        """
        :rtype: int
        """
        smallest = self.nodeList[-1].val
        parent = self.nodeList.pop()
        temp =  parent.right  # If the new last node has right child, named temp
        while temp:
            self.nodeList.append(temp)  # Add left children of temp node
            temp = temp.left
        
        return smallest
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

# ------------------------------
# Summary:
# Use the idea of stack.
# I difine a value self.nodeList to store every node I traverse, the smaller the number the later the node in
# the list. Every time return the last number when next() is called. Pop the current last number, and add new 
# node to the list if new last node has right children. All the new nodes should be smaller than the right 
# child of new last node.
# Binary search tree: all the left nodes are smaller, and all the right nodes are larger (if not null).
# 