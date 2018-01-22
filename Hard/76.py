# ------------------------------
# 76. Minimum Window Substring
# 
# Description:
# Given a string S and a string T, find the minimum window in S which will contain all the 
# characters in T in complexity O(n).
# 
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".
# 
# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there are multiple such windows, you are guaranteed that there will always be only one 
# unique minimum window in S.
# 
# Version: 1.0
# 01/21/18 by Jianfa
# ------------------------------

from collections import defaultdict
import sys
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        chardict = defaultdict(int)
        
        for c in t:
            chardict[c] += 1
        
        begin = end = head = 0
        minInt = len(s) + 1
        counter = len(t)
        
        while end < len(s):
            char = s[end]
            end += 1
            if chardict[char] > 0:
                counter -= 1
            
            chardict[char] -= 1
            
            while counter == 0:
                windowSize = end - begin
                if windowSize < minInt:
                    head = begin
                    minInt = windowSize
                
                head_char = s[begin]
                if chardict[head_char] == 0:
                    counter += 1
                chardict[head_char] += 1
                begin += 1
        
        return "" if minInt == len(s) + 1 else s[head:head+minInt]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow the idea from https://discuss.leetcode.com/topic/30941/here-is-a-10-line-template-that-can-solve-most-substring-problems
# But implemented in python.