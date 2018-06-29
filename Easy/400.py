# ------------------------------
# 400. Nth Digit
# 
# Description:
# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).
# Example 1:
# Input:
# 3
# Output:
# 3
# 
# Example 2:
# Input:
# 11
# Output:
# 0
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
# 
# Version: 1.0
# 06/28/18 by Jianfa
# ------------------------------

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 0
        while n > (digit + 1) * 9 * pow(10, digit):
            n -= (digit + 1) * 9 * pow(10, digit)
            digit += 1
        
        rest = n % (digit + 1)
        num = n / (digit + 1) + pow(10, digit) - 1
        
        if rest == 0:
            return int(str(num)[-1])
        
        else:
            return int(str(num+1)[rest-1])
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 1 - 9: 1 * 9 * 10^0
# 10 - 99: 2 * 9 * 10^1
# 100 - 999: 3 * 9 * 10^2
# 1000 - 9999: 4 * 9 * 10^3
# ...