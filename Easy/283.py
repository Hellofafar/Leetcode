# ------------------------------
# 283. Move Zeroes
# 
# Description:
# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.
# 
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, 
# nums should be [1, 3, 12, 0, 0].
# 
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
# Version: 1.0
# 10/05/17 by Jianfa
# ------------------------------

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for n in nums:
            if n != 0:
                nums[i] = n
                i += 1
        nums[i:-1] = [0 for j in range(len(nums) - i)]


# ------------------------------
# Summary:
# O(n) solution with O(1) space. Traverse every number and if it's not 0, then assign it to pointer's
# position, and move pointer ahead. In the end set all the rest to 0.