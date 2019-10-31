# ------------------------------
# 415. Add Strings
# 
# Description:
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
# 
# Version: 2.0
# 10/30/19 by Jianfa
# ------------------------------

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        a = len(num1) - 1
        b = len(num2) - 1
        
        res = ""
        carry = 0
        while a >= 0 or b >= 0 or carry == 1:
            x = ord(num1[a]) - ord('0') if a >= 0 else 0
            y = ord(num2[b]) - ord('0') if b >= 0 else 0
            digitSum = x + y + carry
            res = str(digitSum)[-1] + res
            carry = digitSum // 10
            a -= 1
            b -= 1
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# More concise solution from: https://leetcode.com/problems/add-strings/discuss/90436/Straightforward-Java-8-main-lines-25ms
# 
# O(m) time, O(1) space, where m is max(len(num1), len(num2))