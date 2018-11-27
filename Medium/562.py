# ------------------------------
# 562. Longest Line of Consecutive One in Matrix
# 
# Description:
# Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
# Example:
# Input:
# [[0,1,1,0],
#  [0,1,1,0],
#  [0,0,0,1]]
# Output: 3
# Hint: The number of elements in the given matrix will not exceed 10,000.
# 
# Version: 1.0
# 11/24/18 by Jianfa
# ------------------------------

class Solution:
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        
        res = 0
        dp = [[[0 for i in range(len(M[0]))] for j in range(len(M))] for k in range(4)]
        
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    dp[0][i][j] = dp[0][i][j-1] + 1 if j > 0 else 1
                    dp[1][i][j] = dp[1][i-1][j] + 1 if i > 0 else 1
                    dp[2][i][j] = dp[2][i-1][j-1] + 1 if i > 0 and j > 0 else 1
                    dp[3][i][j] = dp[3][i-1][j+1] + 1 if (i > 0 and j < len(M[0]) - 1) else 1
                    
                    res = max(res, dp[0][i][j], dp[1][i][j], dp[2][i][j], dp[3][i][j])
                    
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Dp solution from Solution section.