# ------------------------------
# 405. Convert a Number to Hexadecimal
# 
# Description:
# Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.
# Note:
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the number to hex directly.
# 
# Example 1:
# Input:
# 26
# Output:
# "1a"
# 
# Example 2:
# Input:
# -1
# Output:
# "ffffffff"
# 
# Version: 1.0
# 07/01/18 by Jianfa
# ------------------------------

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        
        char = '0123456789abcdef'
        res = ''
        for i in range(8):
            res = char[num & 15] + res
            num = num >> 4
        
        return res.lstrip('0')

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# For python, when num is -1, num >> will always be -1 so loop time needs to be limited.