# ------------------------------
# 486. Predict the Winner
# 
# Description:
# Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.
# Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.
# 
# Example 1:
# Input: [1, 5, 2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2. 
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
# Hence, player 1 will never be the winner and you need to return False.
# 
# Note:
# 1 <= length of the array <= 20.
# Any scores in the given array are non-negative integers and will not exceed 10,000,000.
# If the scores of both players are equal, then player 1 is still the winner.
# 
# Version: 1.0
# 10/17/18 by Jianfa
# ------------------------------

class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Dynamic Programming solution
        # O(n^2) space complexity, O(n^2) time complexity
        if len(nums) == 1:
            return True
        
        dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
        
        currSum = sum(nums)
        player1 = self.helper(nums, dp, currSum, 0, len(nums) - 1)
        player2 = currSum - player1
        return player1 >= player2
        
    def helper(self, nums, dp, currSum, s, e):
        # Return the max price for one player when he starts to pick number between nums[s] and nums[e]
        if s == e:
            dp[s][e] = nums[s]
            return dp[s][e]
        
        if dp[s+1][e] >= 0:  # candidate1: dp[s][e] = nums[s] + dp[s+1][e]
            maxCandidate1 = currSum - dp[s+1][e]
        else:
            maxCandidate1 = currSum - self.helper(nums, dp, currSum - nums[s], s+1, e)
        
        if dp[s][e-1] >= 0:  # candidate2: dp[s][e] = nums[e] + dp[s][e-1]
            maxCandidate2 = currSum - dp[s][e-1]
        else:
            maxCandidate2 = currSum - self.helper(nums, dp, currSum - nums[e], s, e-1)
        
        dp[s][e] = max(maxCandidate1, maxCandidate2)
        return dp[s][e]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Dynamic programming solution.