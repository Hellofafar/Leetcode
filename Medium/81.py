# ------------------------------
# 81. Search in Rotated Sorted Array II
# 
# Description:
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
# 
# Would this affect the run-time complexity? How and why?
# 
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Write a function to determine if a given target is in the array.
# The array may contain duplicates.
# 
# Version: 1.0
# 01/27/18 by Jianfa
# ------------------------------

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                 return True
                
            elif nums[mid] < nums[high]:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            
            elif nums[mid] > nums[high]:
                if nums[mid] > target and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
                    
            else:
                high -= 1
        
        return False
        

# Used for testing
if __name__ == "__main__":
    test = Solution()
    nums = [1]
    target = 0
    print(test.search(nums, target))

# ------------------------------
# Summary:
# Follow the idea from https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28194.