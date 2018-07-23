# ------------------------------
# 429. N-ary Tree Level Order Traversal
# 
# Description:
# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
# For example, given a 3-ary tree:
# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
# 
# Note:
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.
# 
# Version: 1.0
# 07/14/18 by Jianfa
# ------------------------------

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        visited = [root]
        res = []
        while visited:
            level = []
            for i in range(len(visited)):
                curr = visited.pop(0)
                level.append(curr.val)
                if curr.children:
                    visited += curr.children
            
            res.append(level)
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# BFS.