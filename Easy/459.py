# ------------------------------
# 459. Repeated Substring Pattern
# 
# Description:
# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
# Example 1:
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# 
# Example 2:
# Input: "aba"
# Output: False
# 
# Example 3:
# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
# 
# Version: 1.0
# 07/07/18 by Jianfa
# ------------------------------

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return (s + s)[1:-1].find(s) != -1


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Let S1 = s + s, S2 = S1[1:-1] (without first and last char).
# If s in S2, then s has repeated substring pattern.
# https://leetcode.com/problems/repeated-substring-pattern/discuss/94334/Easy-python-solution-with-explaination