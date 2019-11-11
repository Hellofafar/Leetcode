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
# Version: 2.0
# 11/10/19 by Jianfa
# ------------------------------

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        # find the minimum in the nums which is the rotated pivot
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
                
        rotated = low
        low = 0
        high = len(nums) - 1
        n = len(nums)
        while low <= high:
            mid = (low + high) // 2
            realMid = (mid + rotated) % n # the real mid position, it's like (low + rotated + high + rotated) // 2
            # [4,5,6,7,0,1,2] can be considered as [4,5,6,7,0,1,2,4,5,6,7]
            if nums[realMid] == target:
                return realMid
            elif nums[realMid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution
# 
# First find the index of the smallest value using binary search.
# Then do usual binary search with consideration of rotation.
# 
# O(logN) time O(1) space