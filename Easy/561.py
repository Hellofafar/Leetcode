# ------------------------------
# 561. Array Partition I
# 
# Description:
# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
# Example 1:
# Input: [1,4,3,2]
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
# 
# Note:
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].
# 
# Version: 1.0
# 07/16/18 by Jianfa
# ------------------------------

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# It actually is a math problem. Sort at first, then pick the smaller one in every continuous pair.