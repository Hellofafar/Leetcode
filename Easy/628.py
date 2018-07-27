# ------------------------------
# 628. Maximum Product of Three Numbers
# 
# Description:
# Given an integer array, find three numbers whose product is maximum and output the maximum product.
# Example 1:
# Input: [1,2,3]
# Output: 6
# 
# Example 2:
# Input: [1,2,3,4]
# Output: 24
# 
# Note:
# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
# 
# Version: 1.0
# 07/26/18 by Jianfa
# ------------------------------

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-3] * nums[-2] * nums[-1], nums[0] * nums[1] * nums[-1])


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 