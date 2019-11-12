# ------------------------------
# 200. Number of Islands
# 
# Description:
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island 
# is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.
# 
# Example 1:
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# Example 2:
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
# Version: 4.0
# 11/11/19 by Jianfa
# ------------------------------

class Solution:
    count = 0
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        def dfs(i, j):
            grid[i][j] = '#'
            if i + 1 < m and grid[i+1][j] == '1':
                dfs(i+1, j)
            if j + 1 < n and grid[i][j+1] == '1':
                dfs(i, j+1)
            if i - 1 >= 0 and grid[i-1][j] == '1':
                dfs(i-1, j)
            if j - 1 >= 0 and grid[i][j-1] == '1':
                dfs(i, j-1)
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    self.count += 1
                
        return self.count

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DFS solution.
# Idea from: https://leetcode.com/explore/interview/card/microsoft/31/trees-and-graphs/185/discuss/56340/Python-Simple-DFS-Solution
# 
# O(N) time O(N) space (because recursively generatiing i, j)