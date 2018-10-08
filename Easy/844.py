# ------------------------------
# 844. Backspace String Compare
# 
# Description:
# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:

# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:

# Can you solve it in O(N) time and O(1) space?

# Version: 1.0
# 10/07/18 by Jianfa
# ------------------------------

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = ""
        t = ""
        for x in S:
            if x != '#':
                s += x
            else:
                s = s[:-1]
        
        for y in T:
            if y != '#':
                t += y
            else:
                t = t[:-1]
        
        return s == t

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# O(N) space.