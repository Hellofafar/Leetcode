# ------------------------------
# 264. Ugly Number II
# 
# Description:
# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# Example:
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:  
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
# Version: 1.0
# 09/27/18 by Jianfa
# ------------------------------

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        
        if n == 1:
            return 1
        
        k = [1]
        t2 = t3 = t5 = 0
        for i in range(1, n):
            k.append(min(k[t2] * 2, k[t3] * 3, k[t5] * 5))
            if k[i] == k[t2] * 2:
                t2 += 1
            if k[i] == k[t3] * 3:
                t3 += 1
            if k[i] == k[t5] * 5:
                t5 += 1
        
        return k[n-1]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Smart solution from https://leetcode.com/problems/ugly-number-ii/discuss/69364/My-16ms-C++-DP-solution-with-short-explanation