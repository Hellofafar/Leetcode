# ------------------------------
# 69. Sqrt(x)
# 
# Description:
# Implement int sqrt(int x).
# Compute and return the square root of x.
# x is guaranteed to be a non-negative integer.
# 
# Example 1:
# 
# Input: 4
# Output: 2
# 
# Example 2:
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.
# 
# Version: 1.0
# 01/17/18 by Jianfa
# ------------------------------

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        
        s = 1
        while s * s < x:
            s *= 2  
            
        if s * s == x:
            return s
        
        else:
            for i in range(s/2, s):
                if i * i < x:
                    i += 1
                else:
                    break
            
            if i * i == x:
                return i
            else:
                return i - 1

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Initially I start from 1 to check power value of each number, but exceed limit time. So I make 
# the number times 2 every time to decrease checking number.
# While this problem is best to use binary search.
# Let low = 0, high = x, mid = (low + high + 1) / 2
# if mid * mid <= x:
#    low = mid
# else:
#    high = mid - 1