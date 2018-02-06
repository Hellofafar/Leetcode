# ------------------------------
# 371. Sum of Two Integers
# 
# Description:
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
# 
# Example:
# Given a = 1 and b = 2, return 3.
# 
# Version: 1.0
# 02/05/18 by Jianfa
# ------------------------------

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
#         This would be out of time limit for 1 and -1
#         while b != 0:
#             carry = a & b
#             a = a ^ b
#             b = carry << 1
        
#         return a

        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# It sucks for python... Check explanation on https://leetcode.com/problems/sum-of-two-integers/discuss/84282/Python-solution-with-no-%22+-*%22-completely-bit-manipulation-guaranteed
# And also, the commented solution is from: https://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/
# Finally, here is a very good tutorial about bit manipulation:
# A summary: how to use bit manipulation to solve problems easily and efficiently
# https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary:-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently