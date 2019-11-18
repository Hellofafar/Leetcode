# ------------------------------
# 53. Maximum Subarray
# 
# Description:
# Given an integer array nums, find the contiguous subarray (containing at least one 
# number) which has the largest sum and return its sum.
# 
# Example:
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# Follow up:
# If you have figured out the O(n) solution, try coding another solution using the 
# divide and conquer approach, which is more subtle.
# 
# Version: 2.0
# 10/31/19 by Jianfa
# ------------------------------

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sum = max(max_sum, nums[i])
        
        return max_sum

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DP solution from https://leetcode.com/problems/maximum-subarray/solution/ (Kadane's algorithm)
# Actually similar idea from 53.py.
# 
# O(n) time, O(1) space