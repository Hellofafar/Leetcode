# ------------------------------
# 309. Best Time to Buy and Sell Stock with Cooldown
# 
# Description:
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
# 
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# 
# Example:
# Input: [1,2,3,0,2]
# Output: 3 
# 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Version: 1.0
# 10/05/18 by Jianfa
# ------------------------------

import sys

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        state0 = [0 for _ in range(len(prices))]
        state1 = [0 for _ in range(len(prices))]
        state2 = [0 for _ in range(len(prices))]
        
        state1[0] = -prices[0]
        state2[0] = -sys.maxsize
        
        for i in range(1, len(prices)):
            state0[i] = max(state0[i-1], state2[i-1])
            state1[i] = max(state1[i-1], state0[i-1] - prices[i])
            state2[i] = state1[i-1] + prices[i]
            
        return max(state0[-1], state2[-1])

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DP solution. See explanation from https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)