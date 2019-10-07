# ------------------------------
# 202. Happy Number
# 
# Description:
# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process: Starting with any positive integer, replace 
# the number by the sum of the squares of its digits, and repeat the process until the number equals 1 
# (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which 
# this process ends in 1 are happy numbers.
# 
# Example: 
# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# Version: 1.0
# 06/11/18 by Jianfa
# ------------------------------

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = set()
        while n != 1:
            if n in nums:
                return False
            
            nums.add(n)
            summ = 0
            while n:
                digit = n % 10
                summ += digit * digit
                n /= 10
            
            n = summ
            
        return True
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# While loop is finite since the sum of number is small (e.g 999...9 with 32 '9', the sum is 2592)
# Use set to check if the sum will come to cycle finally.