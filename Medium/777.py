# ------------------------------
# 777. Swap Adjacent in LR String
# 
# Description:
# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.
# Example:
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: True
# 
# Explanation:
# We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# 
# Note:
# 1 <= len(start) = len(end) <= 10000.
# Both start and end will only consist of characters in {'L', 'R', 'X'}.
# 
# Version: 1.0
# 11/13/18 by Jianfa
# ------------------------------

class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        # Solid
        if start.replace('X', '') != end.replace('X', ''):
            return False
        
        # accessibility
        # 'L' can only move left
        t = 0
        for i in range(len(start)):
            if start[i] == 'L':
                while end[t] != 'L':
                    t += 1
                
                if i < t:
                    return False
                
                t += 1
        
        # 'R' can only move right
        t = 0
        for i in range(len(start)):
            if start[i] == 'R':
                while end[t] != 'R':
                    t += 1
                
                if i > t:
                    return False
                
                t += 1
        
        return True

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow solution section: https://leetcode.com/problems/swap-adjacent-in-lr-string/solution/
# O(n) space complexity because of replace() function