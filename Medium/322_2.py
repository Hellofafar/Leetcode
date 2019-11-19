# ------------------------------
# 322. Coin Change
# 
# Description:
# You are given coins of different denominations and a total amount of money amount. Write a 
# function to compute the fewest number of coins that you need to make up that amount. If that 
# amount of money cannot be made up by any combination of the coins, return -1.
# 
# Example 1:
# 
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# 
# Example 2:
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.
# 
# Version: 2.0
# 11/18/19 by Jianfa
# ------------------------------

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, amount+1):
            minCount = sys.maxsize
            for j in range(len(coins)):
                if i >= coins[j]:
                    minCount = min(minCount, dp[i - coins[j]] + 1)
            dp[i] = minCount
        
        return -1 if dp[amount] == sys.maxsize else dp[amount]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DP idea from: https://www.jianshu.com/p/0c2041a55735
# 
# O(N * amount) time O(amount) space, N = len(coins)