# ------------------------------
# 367. Valid Perfect Square
# 
# Description:
# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Note: Do not use any built-in library function such as sqrt.
# Example 1:
# Input: 16
# Returns: True
# 
# Example 2:
# Input: 14
# Returns: False
# 
# Version: 1.0
# 06/26/18 by Jianfa
# ------------------------------

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        
        low = 1
        high = num
        while low <= high:
            mid = (low + high) / 2
            if pow(mid, 2) > num:
                high = mid - 1
                continue
            
            elif pow(mid, 2) < num:
                low = mid + 1
                continue
            
            else:
                return True
        
        return False

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Binary search solution.