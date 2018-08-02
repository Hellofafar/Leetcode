# ------------------------------
# 671. Second Minimum Node In a Binary Tree
# 
# Description:
# Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.
# Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
# If no such second minimum value exists, output -1 instead.
# Example 1:
# Input: 
#     2
#    / \
#   2   5
#      / \
#     5   7
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
# 
# Example 2:
# Input: 
#     2
#    / \
#   2   2
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest value.
# 
# Version: 1.0
# 08/01/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = float('inf')
        minimum = root.val
        
        def dfs(node):
            if node:
                if minimum < node.val < self.ans:
                    self.ans = node.val
                elif minimum == node.val:
                    dfs(node.left)
                    dfs(node.right)
                
        dfs(root)
        return self.ans if self.ans < float('inf') else -1

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# From ad-hoc solution.