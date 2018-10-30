# ------------------------------
# 486. Predict the Winner
# 
# Description:
# 
# Version: 1.0
# 10/28/18 by Jianfa
# ------------------------------

class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [0 for _ in range(len(nums))]  # 1D dp list to store effective score (not sum score) of range ends at some index
        
        # Update dp for every run start from s. e.g. dp[s, e] = nums[s] - dp[s+1, e] or num[e] - dp[s, e-1]. dp[s+1, e] and dp[s, e-1] will only be used once, so we can simply use dp[e] and dp[e-1] to represent them
        for s in range(len(nums) - 1)[::-1]:
            for e in range(s+1, len(nums)):
                a = nums[s] - dp[e]
                b = nums[e] - dp[e-1]
                dp[e] = max(a, b)
        
        return dp[len(nums)-1] >= 0

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# From solution Approach #4: https://leetcode.com/problems/predict-the-winner/solution/