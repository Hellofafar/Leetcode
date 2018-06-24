# ------------------------------
# 263. Ugly Number
# 
# Description:
# Write a program to check whether a given number is an ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# Example 1:
# Input: 6
# Output: true
# Explanation: 6 = 2 × 3
# 
# Example 2:
# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
# 
# Example 3:
# Input: 14
# Output: false 
# Explanation: 14 is not ugly since it includes another prime factor 7.
# 
# Note:
# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range: [−231,  231 − 1].
# 
# Version: 1.0
# 06/23/18 by Jianfa
# ------------------------------

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # if num <= 0:
        #     return False
        
        if num == 1:
            return True
        
        factors = [2, 3, 5]
        while num != 1:
            temp = num
            for i in factors:
                if num % i == 0:
                    num = num / i
                    break
            
            if num == temp:
                return False
        
        return True

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 