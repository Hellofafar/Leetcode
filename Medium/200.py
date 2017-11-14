# ------------------------------
# 200. Number of Islands
# 
# Description:
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# 
# Example 1:
# 11110
# 11010
# 11000
# 00000
# Answer: 1
# 
# Example 2:
# 11000
# 11000
# 00100
# 00011
# Answer: 3
# 
# Version: 1.0
# 11/13/17 by Jianfa
# ------------------------------

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                grid[i][j] = "0"
                map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
                return 1
            return 0
        
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

# ------------------------------
# Summary:
# Copied from discussion.
# The following is another easy understanding idea:
# 
# class Solution(object):
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         if len(grid) == 0: return 0
#         m = len(grid)
#         n = len(grid[0])
#         res = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     res += 1
#                     grid[i][j] = '2'
#                     self.island(i, j, grid, m, n)
#         return res
        
#     def island(self, x, y, grid, m, n):
#         if x + 1 < m and grid[x+1][y] == '1':
#             grid[x+1][y] = '2'
#             self.island(x+1,y,grid, m, n)
#         if y + 1 < n and grid[x][y+1] == '1':
#             grid[x][y+1] = '2'
#             self.island(x,y+1,grid, m, n)
#         if x -1 >=0 and grid[x-1][y] == '1':
#             grid[x-1][y] = '2'
#             self.island(x-1,y,grid, m, n)
#         if y - 1 >= 0 and grid[x][y-1] == '1':
#             grid[x][y-1] = '2'
#             self.island(x,y-1,grid, m, n)