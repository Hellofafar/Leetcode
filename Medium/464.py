# ------------------------------
# 464. Can I Win
# 
# Description:
# In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.
# What if we change the game so that players cannot re-use integers?
# For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.
# Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.
# You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.
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
# 10/15/18 by Jianfa
# ------------------------------

class Solution:
    usedDict = {}  # A map used to store the state of the game. {key : True/False}, key represents a state
    
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False

        if desiredTotal <= 0:
            return True
        
        used = ['0' for _ in range(maxChoosableInteger + 1)]
          
        return self.helper(used, desiredTotal)
    
    def helper(self, used, desiredTotal):
        if desiredTotal <= 0:  # If the desiredTotal <= 0 means total has reached initial target, so lose
            return False
        
        key = self.transform(used)  # key is an integer tranformed by used, representing the selecting situation 
        
        if key not in self.usedDict:  # if this situation didn't appear before
            for n in range(1, len(used)):
                if used[n] != '1':
                    used[n] = '1'
                    if not self.helper(used, desiredTotal - n):
                        self.usedDict[key] = True
                        used[n] = '0'
                        return True
                    
                    used[n] = '0'
            
            self.usedDict[key] = False
        
        return self.usedDict.get(key)
    
    def transform(self, used):
        string = ''.join(used)
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