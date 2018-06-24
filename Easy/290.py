# ------------------------------
# 290. Word Pattern
# 
# Description:
# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
# Example 1:
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# 
# Example 2:
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# 
# Example 3:
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# 
# Version: 1.0
# 06/23/18 by Jianfa
# ------------------------------

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        if len(pattern) != len(words):
            return False
        
        pdict = {}
        for i in range(len(words)):
            if pattern[i] in pdict:
                if pdict[pattern[i]] != words[i]:
                    return False
                
            else:
                if words[i] in pdict.values():
                    return False
                
                pdict[pattern[i]] = words[i]
                
        return True
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 