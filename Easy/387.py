# ------------------------------
# 387. First Unique Character in a String
# 
# Description:
# Given a string, find the first non-repeating character in it and return it's index. 
# If it doesn't exist, return -1.
# 
# Examples:
# s = "leetcode"
# return 0.
# s = "loveleetcode",
# return 2.
# 
# Version: 1.0
# 10/08/17 by Jianfa
# ------------------------------

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char = {}
        candidates = []
        for i, c in enumerate(s):
            if c not in char:
                char[c] = i
                candidates.append(i)
            else:
                if char[c] in candidates:  # If this character is the first duplicate, then delete it in candidates, other ignore
                    candidates.remove(char[c])
        
        if not candidates:  # If there is no unique character
            return -1
        
        else:
            return candidates[0]


# ------------------------------
# Summary:
# O(n) solution.
# Idea from shortest-time (55ms) solution: use s.find(x) to get lowest index of x, and use s.rfind(x) to get highest
# index of x.
# index = []
# for x in set(s):
#     if s.find(x) == s.rfind(x):
#         index.append(s.index(x))
# return min(index) if index else -1