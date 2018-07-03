# ------------------------------
# 415. Add Strings
# 
# Description:
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# Note:
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
# 
# Version: 1.0
# 07/02/18 by Jianfa
# ------------------------------

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        power = 1
        num1 = list(num1)
        num2 = list(num2)
        res = 0
        while num1 and num2:
            res += int(num1.pop()) * power + int(num2.pop()) * power
            power *= 10
            
        while num1:
            res += int(num1.pop()) * power
            power *= 10
        
        while num2:
            res += int(num2.pop()) * power
            power *= 10
            
        return str(res)           

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Instead of using int(), it's better to use ord(n) - ord('0') to get the number