# ------------------------------
# 361. Bomb Enemy
# 
# Description:
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
# Note that you can only put the bomb at an empty cell.
# 
# Example:
# For the given grid
# 
# 0 E 0 0
# E 0 W E
# 0 E 0 0
# 
# return 3. (Placing a bomb at (1,1) kills 3 enemies)
# 
# Version: 1.0
# 11/08/17 by Jianfa
# ------------------------------

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m:
            n = len(grid[0])
        else:
            n = 0
            
        res = 0
        rowcount = 0
        colcount = [0] * n
        for i in range(m):
            for j in range(n):
                if (j == 0 or grid[i][j-1] == "W"):
                    rowcount = 0
                    for k in range(j, n):
                        if grid[i][k] != "W":
                            rowcount += grid[i][k] == "E"
                        else:
                            break
                    
                if (i == 0 or grid[i-1][j] == "W"):
                    colcount[j] = 0
                    for k in range(i, m):
                        if grid[k][j] != "W":
                            colcount[j] += grid[k][j] == "E"
                        else:
                            break
                
                if (grid[i][j] == "0"):
                    res = max(res, rowcount + colcount[j])
        
        return res
        

# ------------------------------
# Summary:
# Go through the matrix. For every line, as long as no meeting a wall, calculate the number of enemies and store
# in a rowcount.
# Same for the column, but the number will be stored in a list colcount[]. Because we traverse line by line.