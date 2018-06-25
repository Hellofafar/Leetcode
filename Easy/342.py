# ------------------------------
# 342. Power of Four
# 
# Description:
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
# 
# Example:
# Given num = 16, return true. Given num = 5, return false.
# 
# Follow up: Could you solve it without loops/recursion?
# 
# Version: 1.0
# 06/24/18 by Jianfa
# ------------------------------

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        binary = bin(num)[2:]
        return list(binary).count('0') % 2 == 0 and list(binary).count('1') == 1       

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Bit manipulation.