# ------------------------------
# 29. Divide Two Integers
# 
# Description:
# Divide two integers without using multiplication, division and mod operator.
# 
# If it is overflow, return MAX_INT.
# 
# Version: 1.0
# 12/18/17 by Jianfa
# ------------------------------

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

# Used for testing
if __name__ == "__main__":
    test = Solution()
    dividend, divisor = 15, 3
    print(test.divide(dividend, divisor))

# ------------------------------
# Summary:
# Solution from "Clear python code" in discuss section.