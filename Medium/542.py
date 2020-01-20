# ------------------------------
# 542. 01 Matrix
# 
# Description:
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
# 
# The distance between two adjacent cells is 1.
# 
# Example 1:
# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
# 
# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
# 
# Example 2:
# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
# 
# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]
# 
# Note:
# 
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
# 
# Version: 1.0
# 01/19/20 by Jianfa
# ------------------------------

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return matrix
        
        m = len(matrix)
        n = len(matrix[0])
        dist = [[sys.maxsize] * n for _ in range(m)]
        
        # fist pass: check for the left and the top
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)
        
        # second pass: check for the bottom and the right
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                if i < m - 1:
                    dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                if j < n - 1:
                    dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
        
        return dist

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# I used BFS solution at first, checking distance for every 1 using BFS, but it's not efficient. 
# According to solution from: https://leetcode.com/problems/01-matrix/solution/ , a better
# idea would be starting from every 0 to update distance of 1s in the matrix.
# 
# But here I used the DP solution from the same link, which is to traverse the matrix twice. 
# Once from upper left to bottom right, once from bottom right to top left. As long as a 1 
# is met, its distance is minimum distance of any neightbour + 1