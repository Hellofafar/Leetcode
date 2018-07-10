# ------------------------------
# 479. Largest Palindrome Product
# 
# Description:
# Find the largest palindrome made from the product of two n-digit numbers.
# Since the result could be very large, you should return the largest palindrome mod 1337.
# Example:
# Input: 2
# Output: 987
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
# Note:
# The range of n is [1,8].
# 
# Version: 1.0
# 07/09/18 by Jianfa
# ------------------------------

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        
        upper = pow(10, n) - 1
        lower = pow(10, n-1)
        
        limit = upper * upper
        firstHalf = limit / pow(10, n)
        
        palindromeFound = False
        while not palindromeFound:
            palindrome = int(str(firstHalf) + str(firstHalf)[::-1])
            
            for i in range(lower, upper+1)[::-1]:
                if palindrome / i > limit or i * i < palindrome: # the second condition is to limit search time
                    break
                
                if palindrome % i == 0:
                    palindromeFound = True
                    break
            
            firstHalf -= 1
        
        return palindrome % 1337

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# The solution is from a java solution: https://leetcode.com/problems/largest-palindrome-product/discuss/96297/Java-Solution-using-assumed-max-palindrom
# But I met Time Limit Exceeded with python.