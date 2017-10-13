# ------------------------------
# 15. 3Sum
# 
# Description:
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.
# 
# Note: The solution set must not contain duplicate triplets.
# For example, given array S = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
# 
# Version: 1.0
# 10/11/17 by Jianfa
# ------------------------------

import itertools

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        count_0 = nums.count(0)
        if count_0 >= 3:
            result.append([0,0,0])
        nums.append(0)
        nums.sort()
        pos_0 = nums.index(0)

        left = set(itertools.combinations(nums[:pos_0], 2))
        for pair in left:
            if -sum(pair) in nums[pos_0:]:
                triplet = list(pair)
                triplet.append(-sum(pair))
                result.append(triplet)
        
        right = set(itertools.combinations(nums[pos_0+1:], 2))
        for pair in right:
            if -sum(pair) in nums[:pos_0]:
                triplet = list(pair)
                triplet.append(-sum(pair))
                result.append(triplet)

        return result
    
        
# Used for test
if __name__ == "__main__":
    test = Solution()
    num = [-1, 0, 1, 2, -1, -4]
    
    print(test.threeSum(num))

# Summary
# My solution meets Time Limit Exceeded. To sort it at first is a good start, but I shouln't do combination, 
# which is time-consuming.
# The following is a good solution from Discuss tab:
# 
# def threeSum(self, nums):
#     res = []
#     nums.sort()
#     for i in range(len(nums)-2):
#         if i > 0 and nums[i] == nums[i-1]:  // Eliminate the continuous same number
#             continue
#         l, r = i+1, len(nums)-1
#         while l < r:
#             s = nums[i] + nums[l] + nums[r]
#             if s < 0:
#                 l +=1 
#             elif s > 0:
#                 r -= 1
#             else:
#                 res.append((nums[i], nums[l], nums[r]))
#                 while l < r and nums[l] == nums[l+1]:  // Eliminate the continuous same number again
#                     l += 1
#                 while l < r and nums[r] == nums[r-1]:
#                     r -= 1
#                 l += 1; r -= 1
#     return res
