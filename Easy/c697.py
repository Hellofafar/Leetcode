# ------------------------------
# c697. Degree of an Array (Weekly Contest 54)
# 
# Description:
# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum 
# frequency of any one of its elements.
# 
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same 
# degree as nums.
# 
# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# 
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6
# 
# Version: 1.0
# 10/14/17 by Jianfa
# ------------------------------

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = []
        count_dict = {}
        for n in nums:
            if n in count_dict:
                count_dict[n] += 1
                count.append(count_dict[n])
            else:
                count_dict[n] = 1
                count.append(count_dict[n])
        
        degree = max(count)
        res = len(nums)
        
        while max(count) == degree:
            last_index = count.index(degree)
            target_int = nums[last_index]
            first_index = nums.index(target_int)
            possible_length = last_index - first_index + 1
            if possible_length < res:
                res = possible_length
            count[last_index] = -1
            
        return res


# ------------------------------
# Summary:
# 