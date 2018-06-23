# ------------------------------
# 242. Valid Anagram
# 
# Description:
# Given two strings s and t , write a function to determine if t is an anagram of s.
# 
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# 
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
# 
# Version: 1.0
# 06/22/18 by Jianfa
# ------------------------------

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sdict = {}
        for i in s:
            if i not in sdict:
                sdict[i] = 1
            
            else:
                sdict[i] += 1
        
        for j in t:
            if j not in sdict:
                return False
            
            else:
                sdict[j] -= 1
                if sdict[j] == 0:
                    del sdict[j]
        
        if len(sdict) != 0:
            return False
        
        return True
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Answer to follow-up:
# Use a hash table instead of a fixed size counter. Imagine allocating a large size array to fit the entire range of unicode characters, which could go up to more than 1 million. A hash table is a more generic solution and could adapt to any range of characters.