# ------------------------------
# 449. Serialize and Deserialize BST
# 
# Description:
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.
# The encoded string should be as compact as possible.
# 
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
# 
# Version: 1.0
# 12/20/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preOrder(root, string):
            if root:
                string += str(root.val) + ' '
                string = preOrder(root.left, string)
                string = preOrder(root.right, string)
            
            return string
        
        return preOrder(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build(minVal, maxVal, valList):
            if len(valList) > 1 and minVal < int(valList[0]) < maxVal:  # len(valList) > 1 is because there will be a '' element at the end of valList
                val = int(valList.popleft())
                root = TreeNode(val)
                root.left = build(minVal, val, valList)
                root.right = build(val, maxVal, valList)
                return root
            
        valList = collections.deque(data.split(' '))
        minVal = -sys.maxsize
        maxVal = sys.maxsize
        return build(minVal, maxVal, valList)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from https://leetcode.com/problems/serialize-and-deserialize-bst/discuss/93171/Python-O(-N-)-solution.-easy-to-understand