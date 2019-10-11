# ------------------------------
# 417. Pacific Atlantic Water Flow
# 
# Description:
# Given an m x n matrix of non-negative integers representing the height of each unit cell in a 
# continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic 
# ocean" touches the right and bottom edges.
# 
# Water can only flow in four directions (up, down, left, or right) from a cell to another one 
# with height equal or lower.
# 
# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
# 
# Note:
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# 
# Example:
# Given the following 5x5 matrix:
# 
#   Pacific ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic
# 
# Return:
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
# 
# Version: 1.0
# 10/10/19 by Jianfa
# ------------------------------

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return
        
        res = []
        n = len(matrix)
        m = len(matrix[0])
        
        pacific = [[False for _ in range(m)] for _ in range(n)]
        atlantic = [[False for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            self.dfs(matrix, pacific, -sys.maxsize, i, 0)
            self.dfs(matrix, atlantic, -sys.maxsize, i, m-1)
        
        for j in range(m):
            self.dfs(matrix, pacific, -sys.maxsize, 0, j)
            self.dfs(matrix, atlantic, -sys.maxsize, n-1, j)
        
        # Look for all coordinates that are visited
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res
        
    def dfs(self, matrix, visited, height, x, y):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or visited[x][y] or matrix[x][y] < height:
            return
        
        visited[x][y] = True
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for d in dir:
            self.dfs(matrix, visited, matrix[x][y], x + d[0], y + d[1])

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/90733/Java-BFS-and-DFS-from-Ocean
# DFS solution, but same idea as 417.py