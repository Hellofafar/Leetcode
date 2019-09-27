# ------------------------------
# 322. Coin Change
# 
# Description:
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# 
# Example 1:
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# 
# Example 2:
# Input: coins = [2], amount = 3
# Output: -1
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.
# 
# Version: 1.0
# 09/26/19 by Jianfa
# ------------------------------

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        count = [0 for _ in range(amount)]
        return self.coinChangeHelper(coins, amount, count)
    
    def coinChangeHelper(self, coins: List[int], amount: int, count: List[int]) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if count[amount-1] != 0:
            # It means there exists coin denominations for amount
            return count[amount-1]
        minRes = sys.maxsize
        for coin in coins:
            res = self.coinChangeHelper(coins, amount - coin, count)
            if res >= 0 and res < minRes - 1:
                minRes = res + 1
                
        count[amount-1] = minRes if minRes != sys.maxsize else -1
        return count[amount-1]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Dynamic Programming solution from: https://leetcode.com/problems/coin-change/solution/
# Main idea is to assume that we know F(S) where some change val_1, val_2, ... for S which is optimal and the 
# last coin's denomination is C. Then the following equation should be true because of optimal substructure 
# of the problem:
# F(S) = F(S - C) + 1
# We compute F(S - c_i) for each possible denomination c_0, c_1, ... c_n-1 and choose the minimum among them.
# The idea of the algorithm is to build the solution of the problem from top to bottom. It applies the idea 
# described above. It use backtracking and cut the partial solutions in the recursive tree, which doesn't lead 
# to a viable solution. Тhis happens when we try to make a change of a coin with a value greater than the 
# amount S. To improve time complexity we should store the solutions of the already calculated subproblems in 
# a table.