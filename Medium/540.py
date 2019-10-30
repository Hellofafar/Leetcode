# ------------------------------
# 540. Single Element in a Sorted Array
# 
# Description:
# You are given a sorted array consisting of only integers where every element appears 
# exactly twice, except for one element which appears exactly once. Find this single 
# element that appears only once.
# 
# Example 1:
# 
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# 
# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
# 
# Note: Your solution should run in O(log n) time and O(1) space.
# 
# Version: 1.0
# 10/29/19 by Jianfa
# ------------------------------

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            if nums[mid] == nums[mid-1]:
                # nums[mid] == nums[mid-1]
                if (mid - low) % 2 == 1:
                    # if there are odd numbers on left side (including nums[mid-1]), it means single element should be on the right
                    low = mid + 1
                else:
                    high = mid - 2
            else:
                # nums[mid] == nums[mid+1]
                if (high - mid) % 2 == 1:
                    # if there are odd numbers on right side (including nums[mid+1]), it means single element should be on the right
                    high = mid - 1
                else:
                    low = mid + 2
        
        return nums[low]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Binary search solution, based on the numbers count on left or right side
# 
# O(log n) time, O(1) space