# ------------------------------
# 343. Integer Break
# 
# Description:
# Given a positive integer n, break it into the sum of at least two positive integers and maximize 
# the product of those integers. Return the maximum product you can get.
# 
# Example 1:
# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# 
# Example 2:
# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# Note: You may assume that n is not less than 2 and not larger than 58.
# 
# Version: 1.0
# 09/28/19 by Jianfa
# ------------------------------

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        product = 1
        while n > 4:
            product *= 3
            n -= 3
        product *= n
        
        return product

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from: https://leetcode.com/problems/integer-break/discuss/80689/A-simple-explanation-of-the-math-part-and-a-O(n)-solution
# Main idea is to prove factor should be less than 4 (4 can be considered as 2 * 2), and there should not be more than two 2s contained in product
