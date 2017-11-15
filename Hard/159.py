# ------------------------------
# 159. Longest Substring with At Most Two Distinct Characters
# 
# Description:
# Given a string, find the length of the longest substring T that contains at most 2 distinct characters.
# 
# For example, Given s = “eceba”,
# 
# T is "ece" which its length is 3.
# 
# Version: 1.0
# 11/14/17 by Jianfa
# ------------------------------

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        charDict = {}
        res = 0
        lowest = 0
        
        for i, c in enumerate(s):
            charDict[c] = i
            if len(charDict) > 2:
                lowest = min(charDict.values())
                del charDict[s[lowest]]
                lowest += 1
            res = max(i - lowest + 1, res)
        
        return res
        

# ------------------------------
# Summary:
# Same idea as problem 340. Use hash table to store latest index for a character, use pointer to record the
# start index of a candidate string.