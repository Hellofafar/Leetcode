# ------------------------------
# 494. Target Sum
# 
# Description:
# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 
# 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
# 
# Find out how many ways to assign symbols to make sum of integers equal to target S.
# 
# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# 
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
# 
# Version: 1.0
# 10/24/19 by Jianfa
# ------------------------------

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        
        size = len(nums)
        # Use dictionary to memorize count of the ways periodcally
        # {index: {target: count}} means the count of ways to make the sum of nums[index:] to be target
        countDict = collections.defaultdict(lambda: collections.defaultdict(int))
            
        return self.helper(nums, 0, S, countDict)  
        
    def helper(self, nums, index, S, countDict):
        if index == len(nums):
            return 1 if S == 0 else 0
        
        if S in countDict[index]:
            return countDict[index][S]
        
        add = self.helper(nums, index + 1, S - nums[index], countDict)
        subtract = self.helper(nums, index + 1, S + nums[index], countDict)
        countDict[index][S] = add + subtract
        
        return countDict[index][S]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# At first I use basic recursion without storing the calculation result, I met TLE.
# Then I followed the idea from https://leetcode.com/problems/target-sum/solution/
# to implement recursion with memoization.
#
# O(l * n) time l is range of S, n is the size of nums (NOTE: This is the result from
# solution when using an array rather than a map to store sum result)
# O(n) space the depth of recursion tree can go upto n