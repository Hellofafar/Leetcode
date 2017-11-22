# ------------------------------
# 55. Jump Game
# 
# Description:
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# 
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
# 
# For example:
# A = [2,3,1,1,4], return true.
# A = [3,2,1,0,4], return false.
# 
# Version: 1.0
# 11/21/17 by Jianfa
# ------------------------------

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        if len(nums) == 1:
            return True
        
        pos = 0
        while pos < len(nums) - 1:
            if nums[pos] == 0:
                return False
            
            if pos + nums[pos] >= len(nums) - 1:
                return True
            
            farthest = 0
            next_pos = pos
            for i in range(pos+1, pos + nums[pos] + 1):
                if i - pos + nums[i] > farthest:
                    farthest = i - pos + nums[i]
                    next_pos = i
            pos = next_pos
        

# Used for testing
if __name__ == "__main__":
    test = Solution()
    nums = [0]

    print(test.canJump(nums))

# ------------------------------
# Summary:
# Used greedy idea to move to a position that may reach farthest position.
# Note that nums may include only one item.
