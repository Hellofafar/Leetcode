# ------------------------------
# 34. Search for a Range
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
# 10/24/17 by Jianfa
# ------------------------------

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid - 1
            
            elif nums[mid] < target:
                left = mid + 1
            
            else:
                break
            
        if left > right:
            return [-1, -1]
            
        tmp_m = mid
        while left <= tmp_m:
            if nums[(left + tmp_m) / 2] == target:
                tmp_m = (left + tmp_m) / 2 - 1
            
            else:
                left += 1
               
        tmp_m = mid
        while right >= tmp_m:
            if nums[(right + tmp_m) / 2] == target:
                tmp_m = (right + tmp_m) / 2 + 1
            
            else:
                right -= 1
        
        return [left, right]

# Used for test
if __name__ == "__main__":
    test = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    
    print(test.searchRange(nums, target))

# ------------------------------
# Summary:
# Binary search.