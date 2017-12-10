# ------------------------------
# 417. Pacific Atlantic Water Flow
# 
# Description:
# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, 
# the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the 
# right and bottom edges.
# 
# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height 
# equal or lower.
# 
# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
# 
# Version: 1.0
# 12/09/17 by Jianfa
# ------------------------------

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        if not matrix or not matrix[0]:
            return res
        
        m = len(matrix)
        n = len(matrix[0])
        
        pVisited = []
        aVisited = []
        for i in range(m):
            pVisited.append([False for j in range(n)])
            aVisited.append([False for j in range(n)])
        
        pQueue = []
        aQueue = []
        
        for i in range(m):
            pQueue.append((i, 0))
            aQueue.append((i, n-1))
            pVisited[i][0] = True
            aVisited[i][n-1] = True
            
        
        for j in range(n):
            pQueue.append((0, j))
            aQueue.append((m-1, j))
            pVisited[0][j] = True
            aVisited[m-1][j] = True
            
        for i in range(m):
            self.bfs(matrix, pQueue, pVisited)
            self.bfs(matrix, aQueue, aVisited)
        
        for a in range(m):
            for b in range(n):
                if pVisited[a][b] and aVisited[a][b]:
                    res.append([a, b])
        
        return res
    
    def bfs(self, matrix, queue, visited):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        r = len(matrix)
        c = len(matrix[0])

        while queue:
            item = queue.pop(0)
            x = item[0]
            y = item[1]
            for d in dirs:
                tx = x + d[0]
                ty = y + d[1]
                if tx < 0 or tx >= r or ty < 0 or ty >= c or visited[tx][ty] or matrix[tx][ty] < matrix[x][y]:
                    continue
                
                queue.append((tx, ty))
                visited[tx][ty] = True

# Used for testing
if __name__ == "__main__":
    test = Solution()
    matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

    res = test.pacificAtlantic(matrix)
    print(res)

# ------------------------------
# Summary:
# BFS solution.
# Get the idea from "Java BFS & DFS from Ocean" in discussion section but implementing in Python
# 1. Two Queue and add all the Pacific border to one queue; Atlantic border to another queue.
# 2. Keep a visited matrix for each queue. In the end, add the cell visited by two queue to the result.
# BFS: Water flood from ocean to the cell. Since water can only flow from high/equal cell to low cell, add 
# the neighboor cell with height larger or equal to current cell to the queue and mark as visited.
# Procedure:
# 1. Check if input valid
# 2. Define two matrix to record visited state, and two queues used to do bfs scan (for two oceans respectively)
# 3. Do bfs to find visited point for two oceans
# 4. Check two visited matries to select the point with both "true"