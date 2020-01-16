# ------------------------------
# 522. Longest Uncommon Subsequence II
# 
# Description:
# Given a list of strings, you need to find the longest uncommon subsequence among them. 
# The longest uncommon subsequence is defined as the longest subsequence of one of these 
# strings and this subsequence should not be any subsequence of the other strings.
# 
# A subsequence is a sequence that can be derived from one sequence by deleting some 
# characters without changing the order of the remaining elements. Trivially, any string 
# is a subsequence of itself and an empty string is a subsequence of any string.
# 
# The input will be a list of strings, and the output needs to be the length of the longest 
# uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.
# 
# Example 1:
# Input: "aba", "cdc", "eae"
# Output: 3
# Note:
# 
# All the given strings' lengths will not exceed 10.
# The length of the given list will be in the range of [2, 50].
# 
# Version: 1.0
# 01/15/19 by Jianfa
# ------------------------------

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(s1, s2):
            # check if s1 is subsequence of s2
            i = 0
            for c in s2:
                if i < len(s1) and s1[i] == c:
                    i += 1
            return i == len(s1)
        
        strs.sort(key=len, reverse=True)
        for i, w1 in enumerate(strs):
            if all(not isSubsequence(w1, w2)
                   for j, w2 in enumerate(strs) if i != j):
                # in strs[:i], all w2 must be longer than w1
                return len(w1)
        
        return -1

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Solution from: https://leetcode.com/problems/longest-uncommon-subsequence-ii/discuss/99453/Python-Simple-Explanation