# ------------------------------
# 504. Base 7
# 
# Description:
# Given an integer, return its base 7 string representation.
# Example 1:
# Input: 100
# Output: "202"
# 
# Example 2:
# Input: -7
# Output: "-10"
# Note: The input will be in range of [-1e7, 1e7].
# 
# Version: 1.0
# 07/12/18 by Jianfa
# ------------------------------

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        
        flag = 1 if num > 0 else -1
        num = abs(num)
        power = 0
        while pow(7, power) <= num:
            power += 1
        
        res = ""
        for i in range(power)[::-1]:
            res += str(num / pow(7, i))
            num = num % pow(7, i)
        
        if flag == 1:
            return res
        
        else:
            return "-" + res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Note that condition for power is pow(7, i) <= num rather than pow(7, i) < num