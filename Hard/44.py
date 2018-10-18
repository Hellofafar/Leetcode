# ------------------------------
# 44. Wildcard Matching
# 
# Description:
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
# 
# Note:
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# 
# Version: 1.0
# 10/17/18 by Jianfa
# ------------------------------

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sp = pp = 0   # Initialize s pointer and p pointer
        starIdx = -1  # Record the index of last '*' appeared in pattern
        match = 0     # Match control the index of characters in string that matched to '*'
        while sp < len(s):
            if pp < len(p) and (s[sp] == p[pp] or p[pp] == '?'):
                sp += 1
                pp += 1
                
            elif pp < len(p) and p[pp] == '*':
                starIdx = pp
                pp += 1
                match = sp
                
            elif starIdx >= 0:
                pp = starIdx + 1
                match += 1
                sp = match
            
            else:
                return False
        
        while pp < len(p) and p[pp] == '*':
            pp += 1
        
        return pp == len(p)
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow idea from https://leetcode.com/problems/wildcard-matching/discuss/17810/Linear-runtime-and-constant-space-solution