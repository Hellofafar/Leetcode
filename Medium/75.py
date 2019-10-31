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
# 10/06/17 by Jianfa
# ------------------------------

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        
        l = 0
        while l < len(nums) and nums[l] == 0:
            l += 1
        
        r = len(nums) - 1
        while r >= 0 and nums[r] == 2:
            r -= 1
               
        i = l
        while i <= r:
            if nums[i] == 0:        
                nums[i] = nums[l]
                nums[l] = 0
                l += 1
                i += 1

            elif nums[i] == 2:
                nums[i] = nums[r]
                nums[r] = 2
                r -= 1
            
            else:
                i += 1
                
            
# Used for test
if __name__ == "__main__":
    test = Solution()
    nums = [2,0]

    test.sortColors(nums)

    print(nums)

# ------------------------------
# Summary:
# O(n) solution.
# Set l, i, r pointer. Move l forward to the first position that is not 0, move r backward to the first position
# that is not 2.
# While i <= r, do judgement
#     if meeting a "0", exchange number in l and i, then move 1 step both l and i (note)
#     if meeting a "1", move i
#     if meeting a "2", exchange number in r and i, then just move r 1 step back!! (just r) 