# ------------------------------
# 259. 3Sum Smaller
# 
# Description:
# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n 
# that satisfy the condition nums[i] + nums[j] + nums[k] < target.
# 
# For example, given nums = [-2, 0, 1, 3], and target = 2.
# Return 2. Because there are two triplets which sums are less than 2:
# 
# [-2, 0, 1]
# [-2, 0, 3]
# 
# Version: 1.0
# 11/14/17 by Jianfa
# ------------------------------

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        
        count = 0
        for i in range(len(nums) - 2):
            newTarget = target - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < newTarget:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        
        return count


# ------------------------------
# Summary:
# O(n^2) solution. The idea is to sort the nums at first. Then for every number from the least one, set a new
# target by target - nums[i]. Set two pointer for the rest number, calculate the possible pairs.
# E.g. [1,2,3,4,5] target is 9
# For 1, the new target is 8. since 2 + 5 < 8, so there are three possible pairs: (2,3), (2,4), (2,5) when
# when left = 2.
# More details can refer the solution section.