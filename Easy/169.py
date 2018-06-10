# ------------------------------
# 169. Majority Element
# 
# Description:
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.
# Example 1:
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# Version: 1.0
# 06/09/18 by Jianfa
# ------------------------------

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) / 2]
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# A very smart provided solution.
# Sort the list at first, then the number in index ⌊n/2⌋ will be the answer