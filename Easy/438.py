# ------------------------------
# 438. Find All Anagrams in a String
# 
# Description:
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
# The order of output does not matter.
# Example 1:
# Input:
# s: "cbaebabacd" p: "abc"
# Output:
# [0, 6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# Example 2:
# Input:
# s: "abab" p: "ab"
# Output:
# [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# Version: 1.0
# 07/04/18 by Jianfa
# ------------------------------

from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        
        res = []
        pcounter = Counter(p)
        scounter = Counter(s[:len(p) - 1])
        
        for i in range(len(p) - 1, len(s)):
            scounter[s[i]] += 1
            if scounter == pcounter:
                res.append(i-len(p)+1)
            
            scounter[s[i-len(p)+1]] -= 1
            if scounter[s[i-len(p)+1]] == 0:
                del scounter[s[i-len(p)+1]]
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow the solution from: https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92009/Python-Sliding-Window-Solution-using-Counter/151247