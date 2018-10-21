# ------------------------------
# 324. Wiggle Sort II
# 
# Description:
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
# 
# Example 1:
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
# 
# Example 2:
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].
# 
# Note:
# You may assume all input has valid answer.
# 
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space? 
# 
# Version: 1.0
# 10/20/18 by Jianfa
# ------------------------------

class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = (len(nums) + 1) // 2
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# See https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof