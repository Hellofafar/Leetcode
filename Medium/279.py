# ------------------------------
# 279. Perfect Squares
# 
# Description:
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) 
# which sum to n.
# 
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
# 
# Version: 1.0
# 12/09/17 by Jianfa
# ------------------------------

import math

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        
        countPerfectNum = [0]
        
        while len(countPerfectNum) <= n:
            m = len(countPerfectNum)
            countMin = m
            for i in range(1, int(math.sqrt(m)) + 1):  # Note: don't forget the plus 1 after int(math.sqrt(m))
                countMin = min(countMin, countPerfectNum[m - i * i] + 1)
            
            countPerfectNum.append(countMin)
        
        return countPerfectNum[n]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Dynamic programming solution.
# When calculating the least number for n, I actually calculate all the least number for previous n - 1 integer.
# incrementally. For example for number K, in java script
# for(i=1, i*i <= K, i++){
#     leastNum = min(leastNum, countPerfectNum[K - i*i] + 1); }