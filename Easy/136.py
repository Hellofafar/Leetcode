# ------------------------------
# 136. Single Number
# 
# Description:
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Example 1:
# Input: [2,2,1]
# Output: 1
# 
# Example 2:
# Input: [4,1,2,1,2]
# Output: 4
# 
# Version: 1.0
# 06/08/18 by Jianfa
# ------------------------------

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for n in nums:
            a ^= n
            
        return a

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# From the provided solution: Bit Manipulation
# If we take XOR of zero and some bit, it will return that bit
# a⊕0=a
# If we take XOR of two same bits, it will return 0
# a⊕a=0
# a⊕b⊕a=(a⊕a)⊕b=0⊕b=b