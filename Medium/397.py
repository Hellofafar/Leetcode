# ------------------------------
# 397. Integer Replacement
# 
# Description:
# Given a positive integer n and you can do operations as follow:
# 
# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
# What is the minimum number of replacements needed for n to become 1?
# 
# Example 1:
# Input:
# 8
# Output:
# 3
# Explanation:
# 8 -> 4 -> 2 -> 1
# 
# Example 2:
# Input:
# 7
# Output:
# 4
# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1
# 
# Version: 1.0
# 10/09/19 by Jianfa
# ------------------------------

class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        
        replaceCount = {1:0}
        
        def dp(n: int) -> int:
            if n in replaceCount:
                return replaceCount[n]
            
            if n % 2 == 0:
                res = dp(n / 2) + 1
            else:
                res = min(dp(n + 1), dp(n - 1)) + 1
            
            replaceCount[n] = res
            return res
        
        return dp(n)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Dynamic programming solution.
# While there is another smart math solution idea from: https://leetcode.com/problems/integer-replacement/discuss/87928/Java-12-line-4(5)ms-iterative-solution-with-explanations.-No-other-data-structures.
# When n is even, the operation is fixed. The procedure is unknown when it is odd. When n is 
# odd it can be written into the form n = 2k+1 (k is a non-negative integer.). That is, 
# n+1 = 2k+2 and n-1 = 2k. Then, (n+1)/2 = k+1 and (n-1)/2 = k. So one of (n+1)/2 and (n-1)/2 
# is even, the other is odd. And the "best" case of this problem is to divide as much as 
# possible. Because of that, always pick n+1 or n-1 based on if it can be divided by 4. The 
# only special case of that is when n=3 you would like to pick n-1 rather than n+1.

