# ------------------------------
# 657. Judge Route Circle
# 
# Description:
# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
# The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.
# Example 1:
# Input: "UD"
# Output: true
# 
# Example 2:
# Input: "LL"
# Output: false
# 
# Version: 1.0
# 07/29/18 by Jianfa
# ------------------------------

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        movelist = list(moves)
        return movelist.count('U') == movelist.count('D') and movelist.count('L') == movelist.count('R')

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 