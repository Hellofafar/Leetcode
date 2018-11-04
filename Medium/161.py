# ------------------------------
# 161. One Edit Distance
# 
# Description:
# Given two strings s and t, determine if they are both one edit distance apart.
# Note: 
# There are 3 possiblities to satisify one edit distance apart:
# Insert a character into s to get t
# Delete a character from s to get t
# Replace a character of s to get t
# 
# Example 1:
# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# 
# Example 2:
# Input: s = "cab", t = "ad"
# Output: false
# Explanation: We cannot get t from s by only one step.
# 
# Example 3:
# Input: s = "1203", t = "1213"
# Output: true
# Explanation: We can replace '0' with '1' to get t.
# 
# Version: 1.0
# 11/03/18 by Jianfa
# ------------------------------

class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) < len(t):
                    return s[i:] == t[i+1:]

                elif len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                
                else:
                    return s[i+1:] == t[i:]
        
        return abs(len(s) - len(t)) == 1

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# I at first used two pointers to traverse two list one by one, and count the edit distance of two strings.
# But it's very slow and I get this idea from https://leetcode.com/problems/one-edit-distance/discuss/50098/My-CLEAR-JAVA-solution-with-explanation,
# which is easy to understand.
# You only need to compare the rest of string once a difference is found.