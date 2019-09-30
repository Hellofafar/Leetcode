# ------------------------------
# 375. Guess Number Higher or Lower II
# 
# Description:
# We are playing the Guess Game. The game is as follows:
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.
# However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.
# 
# Example:
# 
# n = 10, I pick 8.
# 
# First round:  You guess 5, I tell you that it's higher. You pay $5.
# Second round: You guess 7, I tell you that it's higher. You pay $7.
# Third round:  You guess 9, I tell you that it's lower. You pay $9.
# 
# Game over. 8 is the number I picked.
# 
# You end up paying $5 + $7 + $9 = $21.
# Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
# 
# Version: 1.0
# 09/29/19 by Jianfa
# ------------------------------

import sys

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        table = [[0] * (n+1) for _ in range(n+1)]
        return self.dp(table, 1, n)
    
    def dp(self, t: List[List[int]], s: int, e: int) -> int:
        if s >= e:
            return 0
        
        if t[s][e] != 0:
            return t[s][e]
        
        res = sys.maxsize
        for x in range(s, e+1):    
            tmp = x + max(self.dp(t, s, x-1), self.dp(t, x+1, e))  # result_when_pick_x = x + max{DP([i~x-1]), DP([x+1, j])}
            res = min(tmp, res)  # DP([i~j]) = min{xi, ... ,xj}
        
        t[s][e] = res
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from: https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/84764/Simple-DP-solution-with-explanation~~
# For each number x in range[i~j]
# we do: result_when_pick_x = x + max{DP([i~x-1]), DP([x+1, j])}
# --> // the max means whenever you choose a number, the feedback is always bad and therefore leads you to a worse branch.
# then we get DP([i~j]) = min{xi, ... ,xj}
# --> // this min makes sure that you are minimizing your cost.