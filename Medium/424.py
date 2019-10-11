# ------------------------------
# 424. Longest Repeating Character Replacement
# 
# Description:
# Given a string s that consists of only uppercase English letters, you can perform at 
# most k operations on that string.
# 
# In one operation, you can choose any character of the string and change it to any 
# other uppercase English character.
# 
# Find the length of the longest sub-string containing all repeating letters you can 
# get after performing the above operations.
# 
# Note:
# Both the string's length and k will not exceed 104.
# 
# Example 1:
# Input:
# s = "ABAB", k = 2
# Output:
# 4
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
# 
# Example 2:
# Input:
# s = "AABABBA", k = 1
# Output:
# 4
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# 
# Version: 1.0
# 10/10/19 by Jianfa
# ------------------------------

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        count = [0 for _ in range(26)]
        maxCount = 0
        maxLength = 0
        start = 0
        
        for end in range(length):
            idx = ord(s[end]) - 65
            count[idx] += 1
            maxCount = max(maxCount, count[idx])
            if end - start + 1 - maxCount > k:
                # there exists more than k characters are different from max-count character
                count[ord(s[start]) - 65] -= 1
                start += 1
            
            maxLength = max(maxLength, end - start + 1)
        
        return maxLength

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Sliding windows idea from: https://leetcode.com/problems/longest-repeating-character-replacement/discuss/91271/Java-12-lines-O(n)-sliding-window-solution-with-explanation
# Note: maxCount may be invalid at some points, but this doesn't matter, because it was 
# valid earlier in the string, and all that matters is finding the max window that 
# occurred anywhere in the string. Additionally, it will expand if and only if enough 
# repeating characters appear in the window to make it expand. So whenever it expands, 
# it's a valid expansion.