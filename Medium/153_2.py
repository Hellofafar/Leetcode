# ------------------------------
# 153. Find Minimum in Rotated Sorted Array
# 
# Description:
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
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
# Version: 2.0
# 11/10/19 by Jianfa
# ------------------------------

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        # at least one side is monotonic increasing,
        # so try to find which side the rotation pivot is on based on if that side is not monotonic increasing
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        return nums[low]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# More concise solution, similar to 153.py