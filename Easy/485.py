# ------------------------------
# 485. Max Consecutive Ones
# 
# Description:
# Given a binary array, find the maximum number of consecutive 1s in this array.
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# 
# Note:
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# 
# Version: 1.0
# 07/09/18 by Jianfa
# ------------------------------

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 not in nums:
            return len(nums)
        
        count = nums.count(0)
        last = -1
        maxLen = 0
        for i in range(count):
            if last == -1:
                index = nums.index(0)
                tempLen = index - last - 1            
            
            else:
                index = nums[last+1:].index(0)
                tempLen = index
                
            last = last + 1 + index
            if tempLen > maxLen:
                maxLen = tempLen
        
        tempLen = len(nums) - last - 1
        if tempLen > maxLen:
            maxLen = tempLen
        
        return maxLen

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# My idea is to find the maximum distance between two '0' and get the maximum number of consecutive '1'.
# According to others' solution, it seems count number of consecutive '1' directly would be faster.