# ------------------------------
# 303. Range Sum Query - Immutable
# 
# Description:
# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.
# 
# Version: 1.0
# 06/24/18 by Jianfa
# ------------------------------

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.subsum = {}
        for i in range(len(nums)):
            self.subsum[i] = sum(nums[i:])
        self.subsum[len(nums)] = 0
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.subsum[i] - self.subsum[j+1]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# My solution is a little inconvenient.
