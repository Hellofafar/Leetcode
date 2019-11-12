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
# Version: 3.0
# 11/11/19 by Jianfa
# ------------------------------

class UnionFind:
    def __init__(self, grid: List[List[str]]) -> None:
        self.count = 0
        self.parent = []
        self.rank = []
        
        # initialize UnionFind
        m = len(grid)
        n = len(grid[0])
        self.parent = [0] * m * n
        self.rank = [0] * m * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.count += 1
                    self.parent[i * n + j] = i * n + j
                self.rank[i * n + j] = 0
    
    def find(self, index: int) -> int: 
        # path compression
        while index != self.parent[index]:
            self.parent[index] = self.find(self.parent[index])
            index = self.parent[index]
        return index
        
    def union(self, p: int, q: int) -> None:
        # union with rank
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot != qRoot:
            if self.rank[pRoot] >= self.rank[qRoot]:
                self.parent[qRoot] = pRoot
                self.rank[pRoot] += self.rank[qRoot]
            else:
                self.parent[pRoot] = qRoot
                self.rank[qRoot] += self.rank[pRoot]
            self.count -= 1
    
    def getCount(self) -> int:
        return self.count
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        uf = UnionFind(grid)
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # union with around units which is also '1'
                    if i + 1 < m and grid[i+1][j] == '1':
                        uf.union(i * n + j, (i+1) * n + j)
                    if j + 1 < n and grid[i][j+1] == '1':
                        uf.union(i * n + j, i * n + j + 1)
                    if i - 1 >= 0 and grid[i-1][j] == '1':
                        uf.union(i * n + j, (i-1) * n + j)
                    if j - 1 >= 0 and grid[i][j-1] == '1':
                        uf.union(i * n + j, i * n + j - 1)
        
        return uf.getCount()

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Union Find solution from https://leetcode.com/problems/number-of-islands/solution/
# 
# A very good example for learning to use Union Find!!!