# ------------------------------
# 3. Longest Substring Without Repeating Characters
# 
# Description:
# Given a string, find the length of the longest substring without repeating characters.
# 
# Example 1:
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# Example 2:
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# Example 3:
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
# Version: 2.0
# 11/16/19 by Jianfa
# ------------------------------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 # start index of a substring
        charIndex = {}
        
        maxLen = 0
        for i in range(len(s)):
            if s[i] not in charIndex:
                charIndex[s[i]] = i
            elif charIndex[s[i]] >= start:
                # find a repeated character in substring
                maxLen = max(maxLen, i - start) # update maxLen
                start = charIndex[s[i]] + 1
                charIndex[s[i]] = i
            else:
                # charIndex[s[i]] < start, update s[i]
                charIndex[s[i]] = i
        
        maxLen = max(maxLen, len(s) - start)
        return maxLen

# Used for testing
if __name__ == "__main__":
    test = Solution()
    str1 = " "
    str2 = "ab"
    str3 = "b a cbb"

# ------------------------------
# Summary:
# It's not hard to get the idea, but there are many edge cases.
# Don't forget to calculate the maxLen after for loop
# 
# O(N) time O(N) space