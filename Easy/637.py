# ------------------------------
# 637. Average of Levels in Binary Tree
# 
# Description:
# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# 
# Note:
# The range of node's value is in the range of 32-bit signed integer.
# 
# Version: 1.0
# 07/28/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        nodes = [root]
        avg = []
        while nodes:
            level = []
            for i in range(len(nodes)):
                first = nodes.pop(0)
                level.append(first.val)
                if first.left:
                    nodes.append(first.left)
                
                if first.right:
                    nodes.append(first.right)
                
            avg.append(float(sum(level)) / len(level))
        
        return avg

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# BFS solution.