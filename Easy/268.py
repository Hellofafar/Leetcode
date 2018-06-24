# ------------------------------
# 268. Missing Number
# 
# Description:
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# Example 1:
# Input: [3,0,1]
# Output: 2
# 
# Example 2:
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
# 
# Version: 1.0
# 06/23/18 by Jianfa
# ------------------------------

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expected = n * (n + 1) / 2
        return expected - sum(nums)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 