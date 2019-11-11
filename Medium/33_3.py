# ------------------------------
# 33. Search in Rotated Sorted Array
# 
# Description:
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
# Version: 3.0
# 11/10/19 by Jianfa
# ------------------------------

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < nums[high]:
                # if right side is monotonic increasing, 
                # check if target in that range, else on the left side
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            
            else:
                # if left side is monotonic increasing,
                # check if target in that range, else on the right side
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        
        return -1

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Make use of the monotonic feature.
# Every time check whether the target on the left side or right side, using binary search.
# The idea is very similar to 81.py, but there is no duplicate so it's much easier. nums[mid]
# is either greater than nums[low] or smaller than nums[high], or both are true. The situation
# can be divided to nums[mid] == target, nums[mid] < nums[high], and others.
# 
# O(logN) time, O(1) space