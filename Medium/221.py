# ------------------------------
# 221. Maximal Square
# 
# Description:
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
# Example:
# Input: 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Output: 4
# 
# Version: 1.0
# 09/12/18 by Jianfa
# ------------------------------

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        r = len(matrix)
        c = len(matrix[0])
        
        dp = [[0 for _ in range(c)] for _ in range(r)]
        
        maxlen = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxlen = max(maxlen, dp[i][j])
        
        return maxlen * maxlen

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DP solution from https://leetcode.com/problems/maximal-square/solution/
# Key point is build a dp matrix, in which dp[i][j] indicates the side length of the maximum square
# whose bottom right corner is matrix[i][j].
# A better DP solution is using a 1D array to replace the 2D dp array. More detail check the link.