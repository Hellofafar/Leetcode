# ------------------------------
# 305. Number of Islands II
# 
# Description:
# A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# Example:
# Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
# Output: [1,1,2,3]
# 
# Explanation:
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).
# 
# 0 0 0
# 0 0 0
# 0 0 0
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# 
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# 
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# 
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# 
# Follow up:
# Can you do it in time complexity O(k log mn), where k is the length of the positions?
# 
# Version: 1.0
# 11/10/18 by Jianfa
# ------------------------------

class Solution:
    count = 0
    
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent = [-1] * m * n
        rank = [0] * m * n
        
        def initialize(x, y):
            parent[x * n + y] = x * n + y
            rank[x * n + y] += 1
            
        def find(p):
            while p != parent[p]:
                parent[p] = parent[parent[p]]  # path compression
                p = parent[p]
            
            return p
        
        def union(p, q):
            pRoot = find(p)
            qRoot = find(q)
            
            if pRoot != qRoot:
                if rank[pRoot] > rank[qRoot]:  # if size of pRoot greater than size of qRoot, combine qRoot to pRoot
                    parent[qRoot] = pRoot
                    rank[pRoot] += rank[qRoot]
                else:                          # else, combine pRoot to qRoot
                    parent[pRoot] = qRoot
                    rank[qRoot] += rank[pRoot]
                    
                self.count -= 1
        
        res = []
        for i, j in positions:
            initialize(i, j)
            self.count += 1
            for x, y in ([i+1, j], [i, j+1], [i-1, j], [i, j-1]):
                if 0 <= x < m and 0 <= y < n and parent[x*n + y] > -1:
                    union(i*n + j, x*n + y)
            
            res.append(self.count)
        
        return res


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Union find solution.
# Maintain a global variable "count" to record number of islands.