# ------------------------------
# 200. Number of Islands
# 
# Description:
# 
# Version: 2.0
# 08/27/18 by Jianfa
# ------------------------------

class Solution(object):
    count = 0
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
           
        def helper(a, b):
            if 0 <= a < len(grid) and 0 <= b < len(grid[0]) and grid[a][b] == '1':
                grid[a][b] = '2'
                map(helper, (a+1, a-1, a, a), (b, b, b+1, b-1))
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1':
                    self.count += 1
                    helper(i, j)
        
        return self.count
                

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 