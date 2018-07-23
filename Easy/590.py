# ------------------------------
# 590. N-ary Tree Postorder Traversal
# 
# Description:
# Given an n-ary tree, return the postorder traversal of its nodes' values.
# For example, given a 3-ary tree:
# Return its postorder traversal as: [5,6,3,2,4,1].
#  
# Note: Recursive solution is trivial, could you do it iteratively?
# 
# Version: 1.0
# 07/22/18 by Jianfa
# ------------------------------

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.insert(0, node.val)
            stack += node.children
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Inspired by idea from 589.py. Use a stack to add every level of nodes, then pop the node of stack
# and add its value to res.