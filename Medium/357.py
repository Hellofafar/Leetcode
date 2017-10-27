# ------------------------------
# 357. Count Numbers with Unique Digits
# 
# Description:
# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.
# 
# Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
# 
# Version: 1.0
# 10/26/17 by Jianfa
# ------------------------------

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        if n > 10:
            return res
        
        elif n == 0:
            return 1
        
        else:
            for i in range(n):
                digit = 9
                if i == 0:
                    digit = 10
                    res += digit
                else:
                    temp_i = i
                    start = 9
                    while temp_i > 0:
                        digit *= start
                        start -= 1
                        temp_i -= 1
                    res += digit
                    
        return res


# Used for test
if __name__ == "__main__":
    test = Solution()
    n = 0

    print(test.countNumbersWithUniqueDigits(n))

# ------------------------------
# Summary:
# E.g when n = 4, return 9*9*8*7 + 9*9*8 + 9*9 + 10