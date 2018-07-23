# ------------------------------
# 559. Maximum Depth of N-ary Tree
# 
# Description:
# Given a n-ary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# For example, given a 3-ary tree:
# We should return its max depth, which is 3.
# 
# Note:
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.
# 
# Version: 1.0
# 07/15/18 by Jianfa
# ------------------------------

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """    
        if not root:
            return 0
        
        visited = [root]
        level = 0
        while visited:
            level += 1
            for i in range(len(visited)):
                cur = visited.pop(0)
                visited += cur.children
        
        return level

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# BFS solution.