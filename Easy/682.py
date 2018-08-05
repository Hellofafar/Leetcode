# ------------------------------
# 682. Baseball Game
# 
# Description:
# You're now a baseball game point recorder.
# Given a list of strings, each string can be one of the 4 following types:
# Integer (one round's score): Directly represents the number of points you get in this round.
# "+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
# "D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
# "C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
# Each round's operation is permanent and could have an impact on the round before and the round after.
# 
# You need to return the sum of the points you could get in all the rounds.
# 
# Example 1:
# Input: ["5","2","C","D","+"]
# Output: 30
# Explanation: 
# Round 1: You could get 5 points. The sum is: 5.
# Round 2: You could get 2 points. The sum is: 7.
# Operation 1: The round 2's data was invalid. The sum is: 5.  
# Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
# Round 4: You could get 5 + 10 = 15 points. The sum is: 30.
# 
# Version: 1.0
# 08/04/18 by Jianfa
# ------------------------------

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        res = 0
        for i in ops:
            if i == '+':
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            
            elif i == 'C':
                invalid = stack.pop()
                res -= invalid
            
            elif i == 'D':
                res += stack[-1] * 2
                stack.append(stack[-1] * 2)
                
                
            else:
                stack.append(int(i))
                res += int(i)
            
        return res
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Take care of the order of adding to res and appending to stack for i == 'D' or i == '+'.