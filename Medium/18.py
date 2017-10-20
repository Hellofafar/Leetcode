# ------------------------------
# 18. 4Sum
# 
# Description:
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# 
# Note: The solution set must not contain duplicate quadruplets.
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
# 10/17/17 by Jianfa
# ------------------------------

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # Think over here! At first I wrote i += 1, it's wrong.
            possible_rest_three = self.threeSum(nums[i+1:], target - nums[i])
            if possible_rest_three:
                for three_set in possible_rest_three:
                    three_set.insert(0, nums[i])
                    res.append(three_set)
        
        return res
        
    def threeSum(self, nums, target):
        res = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                    
        return res
    
        
# Used for test
if __name__ == "__main__":
    test = Solution()
    nums = [1,0,-1,0,-2,2]
    target = 0
    
    print(test.fourSum(nums, target))

# Summary
# Leverage the idea of 3Sum. Check integer one by one and check 3Sum for the rest.