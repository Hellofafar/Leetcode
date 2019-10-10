# ------------------------------
# 416. Partition Equal Subset Sum
# 
# Description:
# Given a non-empty array containing only positive integers, find if the array can be 
# partitioned into two subsets such that the sum of elements in both subsets is equal.
# 
# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
#  
# Example 1:
# Input: [1, 5, 11, 5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#  
# Example 2:
# Input: [1, 2, 3, 5]
# Output: false
# 
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# Version: 1.0
# 10/09/19 by Jianfa
# ------------------------------

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 == 1:
            return False
        
        summ = int(summ / 2)
        
        n = len(nums)
        dp = [[False for _ in range(summ + 1)] for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = True
            
        for i in range(1, n + 1):
            for j in range(1, summ + 1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]
        
        return dp[n][summ]

# Used for testing
if __name__ == "__main__":
    test = Solution()
    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]

# ------------------------------
# Summary:
# DP solution from: https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592/01-knapsack-detailed-explanation
# 0/1 knapsack problem