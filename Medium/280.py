# ------------------------------
# 280. Wiggle Sort
# 
# Description:
# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
# For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
# 
# Version: 1.0
# 11/14/17 by Jianfa
# ------------------------------

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lessThan = True
        for i in range(len(nums) - 1):
            if lessThan and nums[i] > nums[i+1] or not lessThan and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                
            lessThan = not lessThan

# ------------------------------
# Summary:
# Very simple O(n) idea. Compare every two neighbour number, when they are in right position then exchange them.