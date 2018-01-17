# ------------------------------
# 63. Unique Paths II
# 
# Description:
# Follow up for "Unique Paths":
# 
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
# 
# Version: 1.0
# 01/16/18 by Jianfa
# ------------------------------

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
        
        for m in range(len(obstacleGrid)):
            for n in range(len(obstacleGrid[0])):
                if obstacleGrid[m][n] == 1:
                    obstacleGrid[m][n] = -1
        
        obstacleGrid[0][0] = 1
        for m in range(len(obstacleGrid)):
            for n in range(len(obstacleGrid[0])):
                if m == 0 and n > 0:
                    if obstacleGrid[m][n-1] == -1:
                        obstacleGrid[m][n] = 0
                    elif obstacleGrid[m][n] == -1:
                        obstacleGrid[m][n] = 0
                    else:
                        obstacleGrid[m][n] = obstacleGrid[m][n-1]
                
                elif n == 0 and m > 0:
                    if obstacleGrid[m-1][n] == -1:
                        obstacleGrid[m][n] = 0
                    elif obstacleGrid[m][n] == -1:
                        obstacleGrid[m][n] = 0
                    else:
                        obstacleGrid[m][n] = obstacleGrid[m-1][n]
                
                elif m != 0 and n != 0:
                    if obstacleGrid[m][n] == -1:
                        obstacleGrid[m][n] = 0
                    else:
                        obstacleGrid[m][n] = obstacleGrid[m-1][n] + obstacleGrid[m][n-1]
                        
        return obstacleGrid[m][n]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Think about some edge situation.
# If the start point is 1, then return 0.
# Turn the grid to a state grid at first. When a unit is 1, then I change it to -1, which 
# represents an obstacle state. Then start to counting. When meeting an obstacle, count 0.
# Calculate dynamically.