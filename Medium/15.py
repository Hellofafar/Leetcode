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

# import itertools

# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         result = []
#         count_0 = nums.count(0)
#         if count_0 >= 3:
#             result.append([0,0,0])
#         nums.append(0)
#         nums.sort()
#         pos_0 = nums.index(0)

#         left = set(itertools.combinations(nums[:pos_0], 2))
#         for pair in left:
#             if -sum(pair) in nums[pos_0:]:
#                 triplet = list(pair)
#                 triplet.append(-sum(pair))
#                 result.append(triplet)
        
#         right = set(itertools.combinations(nums[pos_0+1:], 2))
#         for pair in right:
#             if -sum(pair) in nums[:pos_0]:
#                 triplet = list(pair)
#                 triplet.append(-sum(pair))
#                 result.append(triplet)

#         return result

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        if len(nums) < 3:
            return res
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            sum_rest = 0 - nums[i]
            low = i + 1
            high = len(nums) - 1
            while low < high:
                if nums[low] + nums[high] == sum_rest:
                    res.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    while low < high and nums[high] == nums[high-1]:
                        high -= 1
                    low += 1
                    high -= 1
                
                elif nums[low] + nums[high] < sum_rest:
                    low += 1
                
                else:
                    high -= 1
        
        return res
        
# Used for test
if __name__ == "__main__":
    test = Solution()
    num = [-1, 0, 1, 2, -1, -4]
    
    print(test.threeSum(num))

# Summary
# My first solution meets Time Limit Exceeded. To sort it at first is a good start, but I shouln't do combination, 
# which is time-consuming.
# 
# I follow an idea "Concise O(N^2) Java solution" from discuss section.
# The key idea is to run through all indices of a possible first element of a triplet. For each 
# possible first element we make a standard bi-directional 2Sum sweep of the remaining part of 
# the array. Remember to skip equal items to avoid duplicates.