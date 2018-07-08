# ------------------------------
# 463. Island Perimeter
# 
# Description:
# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
# Example:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
# Answer: 16
# 
# Version: 1.0
# 07/07/18 by Jianfa
# ------------------------------

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if j < len(grid[0]) - 1 and grid[i][j+1] == 1:
                        perimeter -= 2
                    
                    if i < len(grid) - 1 and grid[i+1][j] == 1:
                        perimeter -= 2
        
        return perimeter

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Every time if a block is 1, perimeter should add 4.
# Then check the right and lower block of it. Once another '1' block is found, total perimeter minus 2.