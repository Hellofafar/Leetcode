# ------------------------------
# 32. Longest Valid Parentheses
# 
# Description:
# Given a string containing just the characters '(' and ')', find the length of 
# the longest valid (well-formed) parentheses substring.
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
# 
# Another example is ")()())", where the longest valid parentheses substring is 
# "()()", which has length = 4.
# 
# Version: 2.0
# 10/31/19 by Jianfa
# ------------------------------

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLen = 0
        dp = [0] * len(s) # the length of the longest valid substring ending at ith index
        for i in range(1, len(s)):
            if s[i] == ")":
                # valid substring ends with ")"
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2 if i >= 2 else 2
                elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == "(":
                    # if s[i-1] == ")"
                    # check the character at s[i - dp[i-1] - 1] if it's "(", that can match current ")"
                    dp[i] = dp[i - dp[i-1] - 2] + dp[i-1] + 2 if i - dp[i-1] >= 2 else dp[i-1] + 2
                maxLen = max(maxLen, dp[i])
        
        return maxLen

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DP solution from https://leetcode.com/problems/longest-valid-parentheses/solution/
# make use of a dp array where ith element of dp represents the length of the longest 
# valid substring ending at iith index.
# 
# O(n) time, O(n) space