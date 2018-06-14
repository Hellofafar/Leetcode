# ------------------------------
# 205. Isomorphic Strings
# 
# Description:
# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
# 
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# 
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# 
# Example 3:
# Input: s = "paper", t = "title"
# Output: true
# Note:
# You may assume both s and t have the same length.
# 
# Version: 1.0
# 06/12/18 by Jianfa
# ------------------------------

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        
        chardict = {}
        for i in range(len(s)):
            if s[i] not in chardict:
                if t[i] in chardict.values():
                    return False
                chardict[s[i]] = t[i]
            
            else:
                if chardict[s[i]] != t[i]:
                    return False
            
        return True
        

# Used for testing
if __name__ == "__main__":
    test = Solution()
    s = 'ab'
    t = 'aa'
    print(test.isIsomorphic(s, t))

# ------------------------------
# Summary:
# Don't forget the situation that two characters may map to the same character.