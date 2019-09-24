# ------------------------------
# 304. Range Sum Query 2D - Immutable
# 
# Description:
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner 
# (row1, col1) and lower right corner (row2, col2).
# 
# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
# 
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# 
# Note:
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.
# 
# Version: 1.0
# 09/24/18 by Jianfa
# ------------------------------

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.m = 0
            self.n = 0
        else:
            self.m = len(matrix)
            self.n = len(matrix[0])
        
        self.dp = [[0] * (self.n+1) for _ in range(self.m+1)]
        for i in range(self.m):
            for j in range(self.n):
                self.dp[i+1][j+1] = self.dp[i+1][j] + self.dp[i][j+1] + matrix[i][j] - self.dp[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.m == 0 or self.n == 0:
            return None
            
        return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Used for testing
if __name__ == "__main__":
    test = Solution()
    matrix = [[]]
    matrix = [[3, 0, 1, 4, 2],[5, 6, 3, 2, 1],[1, 2, 0, 1, 5],[4, 1, 0, 1, 7],[1, 0, 3, 0, 5]]

# ------------------------------
# Summary:
# Main idea is to cache the summation.
# At first I cached the rows. Every unit represents the sum of previous units.
# This solution is fine but not the optimal, then I checked solution and get the idea to cache sum of region,
# which is a 2-D solution.
# Check https://leetcode.com/problems/range-sum-query-2d-immutable/solution/ for details.