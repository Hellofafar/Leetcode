# ------------------------------
# 665. Non-decreasing Array
# 
# Description:
# Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# 
# Example 2:
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
# 
# Note: The n belongs to [1, 10,000].
# 
# Version: 1.0
# 07/30/18 by Jianfa
# ------------------------------

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = -1
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if count > 1:
                    return False
                
                index = i
        
        return (count == 0 or index == 0 or index == len(nums) - 2 or nums[index-1] <= nums[index+1] or nums[index] <= nums[index + 2])
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# From solution.