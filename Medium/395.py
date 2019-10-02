# ------------------------------
# 395. Longest Substring with At Least K Repeating Characters
# 
# Description:
# Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.
# 
# Example 1:
# Input:
# s = "aaabb", k = 3
# Output:
# 3
# The longest substring is "aaa", as 'a' is repeated 3 times.
# 
# Example 2:
# Input:
# s = "ababbc", k = 2
# Output:
# 5
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
# 
# Version: 1.0
# 10/01/19 by Jianfa
# ------------------------------

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(c))
        return len(s)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87768/4-lines-Python