# ------------------------------
# 464. Can I Win
# 
# Description:
# In the "100 game," two players take turns adding, to a running total, any integer from 
# 1..10. The player who first causes the running total to reach or exceed 100 wins.
# What if we change the game so that players cannot re-use integers?
# For example, two players might take turns drawing from a common pool of numbers of 1..15 
# without replacement until they reach a total >= 100.
# Given an integer maxChoosableInteger and another integer desiredTotal, determine if the 
# first player to move can force a win, assuming both players play optimally.
# You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal 
# will not be larger than 300.
# 
# Example
# Input:
# maxChoosableInteger = 10
# desiredTotal = 11
# 
# Output:
# false
# 
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
# Same with other integers chosen by the first player, the second player will always win.
# 
# Version: 1.0
# 10/15/19 by Jianfa
# ------------------------------

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        
        if desiredTotal <= 0:
            return True
        
        stateDict = {}
        used = ["0"] * (maxChoosableInteger + 1)
        return self.helper(stateDict, used, desiredTotal)
    
    def helper(self, stateDict, used, desiredTotal):
        if desiredTotal <= 0:
            # This mean the rest to desiredTotal, if it <= 0 that means the other has reached desired total
            return False
        
        state = self.transform(used)  # state represen the selection state
        if state not in stateDict:
            for i in range(1, len(used)):
                if used[i] != "1":
                    used[i] = "1"
                    if not self.helper(stateDict, used, desiredTotal - i):
                        # the other player lose so it means I will win
                        stateDict[state] = True
                        used[i] = "0"
                        return True
                    used[i] = "0"
            # Cannot find any solution to win
            stateDict[state] = False
        else:
            return stateDict[state]
        
    def transform(self, used):
        # e.g if used is [0, 1, 0, 1, 0]
        # return will be 1010
        # because used[0] represent using 0, which will always be false so can ignore it
        string = "".join(used)
        return int(string, 2)

# Used for testing
if __name__ == "__main__":
    test = Solution()
    maxChoosableInteger = 15
    desiredTotal = 100
    print(test.canIWin(maxChoosableInteger, desiredTotal))

# ------------------------------
# Summary:
# Follow idea from https://leetcode.com/problems/can-i-win/discuss/95277/Java-solution-using-HashMap-with-detailed-explanation
# 
# O(2^n) time and O(n) space