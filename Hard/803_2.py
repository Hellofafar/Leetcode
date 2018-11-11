# ------------------------------
# 803. Bricks Falling When Hit
# 
# Description:
# 
# Version: 2.0
# 11/10/18 by Jianfa
# ------------------------------

class Solution:
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid[0])
        
        # Connected unconnected '1' bricks
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != 1:  # grid[i][j] is 2 means it's visited or it's no-dropping brick, is 0 means it's empty
                return 0
            
            grid[i][j] = 2
            ret = 1  # Number of connected '1' bricks include itself (not include no-dropping bricks)
            ret += sum(dfs(x, y) for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)))
            
            return ret
        
        # Check whether grid[i][j] is connected to no-dropping brick
        def is_connected(i, j):
            return i == 0 or any(0 <= x < m and 0 <= y < n and grid[x][y] == 2 for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)))
        
        # Record the status of brick after hits
        # if it was 0, now it's -1
        # if if was 1, now it's 0
        for i, j in hits:
            grid[i][j] -= 1
        
        # Get new status of grid after all hits
        for j in range(n):
            dfs(0, j)  # [0, j] is at the top row of grid, if it's 1 then it will not drop
            
        res = []
        for i, j in hits[::-1]:
            grid[i][j] += 1

            if grid[i][j] and is_connected(i, j):
                res.append(dfs(i, j) - 1)  # Minus itself when counting
            else:
                res.append(0)  # Don't forget the situation when there is empty
        
        return res[::-1]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Mainly follow idea from https://leetcode.com/problems/bricks-falling-when-hit/discuss/119829/Python-Solution-by-reversely-adding-hits-bricks-back
# A key point is:
# if a brick is serving as a connecting brick, once it's hitted, then some bricks may fall because of it. If we do dfs search from no-dropping bricks
# at the first row, all the bricks that can be detected are bricks which were not be affected from the hit.
# Which means, if we reverse the process to add a brick BRICK that makes no-dropping bricks connected with other bricks, then the number of "other bricks" is
# actually the number of bricks to drop when BRICK is hitted.