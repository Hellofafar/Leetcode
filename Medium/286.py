# ------------------------------
# 286. Walls and Gates
# 
# Description:
# You are given a m x n 2D grid initialized with these three possible values.
# 
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent 
# INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach 
# a gate, it should be filled with INF.
# 
# Example: 
# 
# Given the 2D grid:
# 
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:
# 
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4
# 
# Version: 1.0
# 10/27/19 by Jianfa
# ------------------------------

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        
        m = len(rooms)
        n = len(rooms[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    # if it's gate, push it to the queue
                    queue.append([i, j])
        
        dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        while queue:
            point = queue.pop(0)
            row = point[0]
            col = point[1]
            for d in dirs:
                r = row + d[0]
                c = col + d[1]
                if 0 <= r < m and 0 <= c < n and rooms[r][c] == 2147483647:
                    # if it's INF value, it means this point hasn't be visited
                    rooms[r][c] = rooms[row][col] + 1
                    queue.append([r, c])

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# BFS solution from https://leetcode.com/problems/walls-and-gates/solution/
# Start of BFS is the gate, then spread out