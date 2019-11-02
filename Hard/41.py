# ------------------------------
# 41. First Missing Positive
# 
# Description:
# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Example 1:
# Input: [1,2,0]
# Output: 3
# 
# Example 2:
# Input: [3,4,-1,1]
# Output: 2
# 
# Example 3:
# Input: [7,8,9,11,12]
# Output: 1
# 
# Note:
# Your algorithm should run in O(n) time and uses constant extra space.
# 
# Version: 1.0
# 11/01/19 by Jianfa
# ------------------------------

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if 1 not in nums:
            return 1
        
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # use index as a key and number sign as a presence detector
        # e.g. if 2 in the nums, then makes nums[1] negetive
        # if 4 in the nums, makes nums[3] negetive
        for i in range(n):
            a = abs(nums[i])
            if 1 < a <= n:
                nums[a-1] = -abs(nums[a-1])
        # traverse the nums again to find the first number is positive,
        # then index + 1 is the smallest missing positive number
        for i in range(1, n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Index as hash key idea from: https://leetcode.com/problems/first-missing-positive/solution/
# O(n) time, O(1) space