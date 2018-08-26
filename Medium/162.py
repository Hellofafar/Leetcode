# ------------------------------
# 162. Find Peak Element
# 
# Description:
# A peak element is an element that is greater than its neighbors.
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that nums[-1] = nums[n] = -∞.
# 
# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# 
# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5 
# Explanation: Your function can return either index number 1 where the peak element is 2, 
#              or index number 5 where the peak element is 6.
# Note:
# Your solution should be in logarithmic complexity.
# 
# Version: 1.0
# 08/25/18 by Jianfa
# ------------------------------

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            if start == end:
                return start
            mid = (start + end) / 2
            if nums[mid] < nums[mid+1]:
                start = mid + 1
            else:
                end = mid

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Binary search solution provided.
# If middle element is on a rising slope, the peak lies towards the right of it.
# If middle element is on a falling slope, the peak lies towards the left of it.