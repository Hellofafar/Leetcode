# ------------------------------
# 75. Sort Colors
# 
# Description:
# Given an array with n objects colored red, white or blue, sort them in-place so that 
# objects of the same color are adjacent, with the colors in the order red, white and 
# blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue 
# respectively.
# 
# Note: You are not suppose to use the library's sort function for this problem.
# 
# Example:
# 
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# 
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array 
# with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
# 
# Version: 1.0
# 10/30/19 by Jianfa
# ------------------------------

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0 
        p2 = len(nums) - 1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[p2], nums[i] = nums[i], nums[p2]
                p2 -= 1
            else:
                i += 1

# ------------------------------
# Summary:
# More concise O(n) solution from https://leetcode.com/problems/sort-colors/solution/
# 
# While i <= p2, do judgement (it's not i < p2)
# if meeting a "0", swap number in p0 and i, then move 1 step both p0 and i
# if meeting a "1", move i
# if meeting a "2", swap number in p2 and i, then move p2 1 step back!! (just p2)
# because after swap there maybe a 0 in the nums[i]