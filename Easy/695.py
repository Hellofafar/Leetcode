# ------------------------------
# 695. Max Area of Island
# 
# Description:
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# 
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# 
# Version: 1.0
# 08/06/18 by Jianfa
# ------------------------------

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        def dfs(m, n, visited):
            if not 0 <= m < len(grid) or not 0 <= n < len(grid[0]) or not grid[m][n] or (m, n) in visited:
                return 0
            
            visited.append((m, n))
            return 1 + dfs(m-1, n, visited) + dfs(m+1, n, visited) + dfs(m, n-1, visited) + dfs(m, n+1, visited)
        
        visited = []
        maxarea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxarea = max(maxarea, dfs(i, j, visited))
        
        return maxarea


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DFS recursive solution. The key point is to simplify 'if' statement using logical operations.