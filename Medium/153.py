# ------------------------------
# 153. Find Minimum in Rotated Sorted Array
# 
# Description:
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Find the minimum element.
# You may assume no duplicate exists in the array.
# 
# Example 1:
# Input: [3,4,5,1,2] 
# Output: 1
# 
# Example 2:
# Input: [4,5,6,7,0,1,2]
# Output: 0
# 
# Version: 1.0
# 08/25/18 by Jianfa
# ------------------------------

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            
            mid = (start + end) / 2
            
            if nums[mid] >= nums[start]:
                # minimum must be at the nums[mid+1, high]
                start = mid + 1
                
            else:
                # minimum must be at the nums[start, mid]
                # low will not be 0
                end = mid

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Binary search solution from https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/48493/Compact-and-clean-C++-solution
# Key point is, if the first member is less than last member, there's no rotation and the first member is the smallest one.
# When the first member is greater than the last member, the smallest one should be in the subarray.