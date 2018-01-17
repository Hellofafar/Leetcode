# ------------------------------
# 64. Minimum Path Sum
# 
# Description:
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example 1:
# [[1,3,1],
#  [1,5,1],
#  [4,2,1]]
# Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.
# 
# Version: 1.0
# 01/17/18 by Jianfa
# ------------------------------

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        minimal = [[0 for j in range(n)] for i in range(m)]
        
        minimal[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j != 0:
                    minimal[i][j] = minimal[i][j-1] + grid[i][j]
                
                elif i != 0 and j == 0:
                    minimal[i][j] = minimal[i-1][j] + grid[i][j]
                    
                elif i != 0 and j != 0:
                    minimal[i][j] = min(minimal[i-1][j], minimal[i][j-1]) + grid[i][j]
            
        return minimal[-1][-1]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Dynamically calculate minimal sum for each unit from up to down, left to right.
# For the first row and first column, initially set the minimal sum based on its previous unit.