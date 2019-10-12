# ------------------------------
# 427. Construct Quad Tree
# 
# Description:
# We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only 
# be true or false. The root node represents the whole grid. For each node, it will be 
# subdivided into four children nodes until the values in the region it represents are all 
# the same.
# 
# Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only 
# if the node is a leaf node. The val attribute for a leaf node contains the value of the 
# region it represents.
# 
# Your task is to use a quad tree to represent a given grid.
# (Check picture from https://leetcode.com/problems/construct-quad-tree/)
# 
# Version: 1.0
# 10/11/19 by Jianfa
# ------------------------------

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid or not grid[0]:
            return None
        
        n = len(grid)
        return self.dfs(grid, 0, 0, n-1, n-1)
        
    def dfs(self, grid, x1, y1, x2, y2):
        # x1, y1 is the coordinates of top left corner
        # x2, y2 is the coordinates of bottom right corner
        if x1 == x2 and y1 == y2:
            return Node(grid[x1][y1], True, None, None, None, None)
        
        # Be careful of the coordinates of each region
        topLeft = self.dfs(grid, x1, y1, (x1 + x2) // 2, (y1 + y2) // 2)
        topRight = self.dfs(grid, x1, (y1 + y2) // 2 + 1, (x1 + x2) // 2, y2)
        bottomLeft = self.dfs(grid, (x1 + x2) // 2 + 1, y1, x2, (y1 + y2) // 2)
        bottomRight = self.dfs(grid, (x1 + x2) // 2 + 1, (y1 + y2) // 2 + 1, x2, y2)
        
        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf \
           and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
            node = Node(topLeft.val, True, None, None, None, None)
        else:
            node = Node("*", False, topLeft, topRight, bottomLeft, bottomRight)
        
        return node

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DFS solution