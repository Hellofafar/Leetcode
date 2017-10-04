# ------------------------------
# 121. Best Time to Buy and Sell Stock
# 
# Description:
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# If you were only permitted to complete at most one transaction (ie, buy one and sell one 
# share of the stock), design an algorithm to find the maximum profit.
# 
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# 
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
# In this case, no transaction is done, i.e. max profit = 0.
# 
# Version: 1.0
# 10/03/17 by Jianfa
# ------------------------------

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        low = prices[0]
        profit = 0
        for n in prices:
            if n < low:
                low = n
            else:
                profit = max(profit, n - low)

        return profit          


# Used for test
if __name__ == "__main__":
    test = Solution()
    prices = [7, 1, 5, 3, 6, 4]

    print(test.maxProfit(prices))


# ------------------------------
# Summary:
# O(n) solution. Replace lowest point if current n is lower, otherwies compare current profit with maximum profit.
# Idea is simple but cost me over half an hour to revise it.