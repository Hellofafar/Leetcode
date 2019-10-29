# ------------------------------
# 516. Longest Palindromic Subsequence
# 
# Description:
# Given a string s, find the longest palindromic subsequence's length in s. You may 
# assume that the maximum length of s is 1000.
# 
# Example 1:
# Input:
# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# 
# Example 2:
# Input:
# "cbbd"
# Output:
# 2
# One possible longest palindromic subsequence is "bb".
# 
# Version: 1.0
# 10/28/19 by Jianfa
# ------------------------------

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        # dp[i][j]: the longest palindromic subsequence's length of substring(i, j), 
        # here i, j represent left, right indexes in the string
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n)[::-1]:
            dp[i][i] = 1
            for j in range(i+1, n):
                # dp[i][j] = dp[i+1][j-1] + 2 if s.charAt(i) == s.charAt(j)
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DP solution from https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99101/Straight-forward-Java-DP-solution
# dp[i][j] = dp[i+1][j-1] + 2 if s.charAt(i) == s.charAt(j)
# otherwise, dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1])
# Initialization: dp[i][i] = 1