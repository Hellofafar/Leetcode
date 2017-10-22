# ------------------------------
# 33. Search in Rotated Sorted Array
# 
# Description:
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# 
# Version: 1.0
# 10/21/17 by Jianfa
# ------------------------------

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        if target not in nums:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) / 2
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                left = mid + 1
            else:
                right = mid
  
        return left if target == nums[left] else -1
                

# Used for test
if __name__ == "__main__":
    test = Solution()
    nums = [3,4,5,1,2]
    
    print(test.search(nums, 5))

# ------------------------------
# Summary:
# There are three conditions need to be thought: nums[0] > target? nums[0] > nums[mid]? target > nums[mid]?
# If exactly two of them are true, then target should be at left side.
# Using XOR to distinguish.