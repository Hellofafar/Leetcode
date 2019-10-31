# ------------------------------
# 154. Find Minimum in Rotated Sorted Array II
# 
# Description:
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# The array may contain duplicates.
# 
# Example 1:
# Input: [1,3,5]
# Output: 1
# 
# Example 2:
# Input: [2,2,2,0,1]
# Output: 0
# 
# Note:
# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?
# 
# Version: 1.0
# 10/30/19 by Jianfa
# ------------------------------

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] > nums[high]:
                low = mid + 1
                
            elif nums[mid] < nums[high]:
                high = mid
            
            else:
                # nums[mid] == nums[high]
                # not sure where the minimum is 
                high -= 1
        
        return nums[low]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/discuss/48808/My-pretty-simple-code-to-solve-it
# corner case: [3, 1, 3]