# ------------------------------
# 567. Permutation in String
# 
# Description:
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation 
# of s1. In other words, one of the first string's permutations is the substring of the second 
# string.
# 
# Example 1:
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# 
# Note:
# 
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
# 
# Version: 1.0
# 01/29/20 by Jianfa
# ------------------------------

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        charDict = collections.defaultdict(int)
        # count the number of each character in s1
        for i in range(len(s1)):
            charDict[s1[i]] += 1
            charDict[s2[i]] -= 1
        
        # check if s2[:len(s1)] satisfies the condition
        if self.allZero(charDict):
            return True
        
        for i in range(len(s1), len(s2)):
            charDict[s2[i]] -= 1
            charDict[s2[i - len(s1)]] += 1
            if self.allZero(charDict):
                return True
        
        return False
        
    def allZero(self, counter: dict) -> bool:
        for key in counter:
            if counter[key] != 0:
                return False
        return True
            

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from: https://leetcode.com/problems/permutation-in-string/discuss/102588/Java-Solution-Sliding-Window
# Counter + sliding window
# O(S) time O(T) space, S is length of s2, T is length of S1 