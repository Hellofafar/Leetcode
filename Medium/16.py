# ------------------------------
# 16. 3Sum Closest
# 
# Description:
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
# 
# For example, given array S = {-1 2 1 -4}, and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2). 
# 
# Version: 1.0
# 10/13/17 by Jianfa
# ------------------------------

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """ 
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                if abs(s - target) < abs(closest - target):
                    closest = s
                
                if s > target:
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1

                elif s < target:
                    while l < r and nums[r] == nums[r - 1]:
                        l += 1
                    l += 1
                
                else:
                    return s
        
        return closest

        
# Used for test
if __name__ == "__main__":
    test = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    
    print(test.threeSumClosest(nums, target))

# Summary
# Similar idea to 15.py
