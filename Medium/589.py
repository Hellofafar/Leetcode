# ------------------------------
# 589. N-ary Tree Preorder Traversal
# 
# Description:
# Given an n-ary tree, return the preorder traversal of its nodes' values. 
# For example, given a 3-ary tree:
# Return its preorder traversal as: [1,3,5,6,2,4].
# Note: Recursive solution is trivial, could you do it iteratively?
# 
# Version: 1.0
# 07/20/18 by Jianfa
# ------------------------------

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            for i in range(len(node.children))[::-1]:
                stack.append(node.children[i])
            
            res.append(node.val)
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Iterative solution. Key point is using stack, and push children node from right to left every one.
# So the left child node will always be the top one in stack.
# From the idea: https://leetcode.com/problems/n-ary-tree-preorder-traversal/discuss/150297/C++-simple-10-line-iterative-solution-beat-100!