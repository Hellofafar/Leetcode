# ------------------------------
# 300. Longest Increasing Subsequence
# 
# Description:
# Given an unsorted array of integers, find the length of longest increasing subsequence.
# 
# Example:
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
# 
# Note:
# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?
# 
# Version: 1.0
# 12/15/18 by Jianfa
# ------------------------------

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        dp = [1]
        maxLen = 1
        for i in range(1, len(nums)):
            maxval = 0  # max length between dp[0:i] (i excluded)
            for j in range(0, i):
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])
            
            dp.append(maxval+1)
            maxLen = max(maxLen, dp[i])
        
        return maxLen

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Dynamic Programming solution from Solution section.