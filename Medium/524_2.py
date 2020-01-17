# ------------------------------
# 524. Longest Word in Dictionary through Deleting
# 
# Description:
# Given a string and a string dictionary, find the longest string in the dictionary that can 
# be formed by deleting some characters of the given string. If there are more than one possible 
# results, return the longest word with the smallest lexicographical order. If there is no 
# possible result, return the empty string.
# 
# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# 
# Output: 
# "apple"
# 
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]
# 
# Output: 
# "a"
# 
# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
# 
# Version: 2.0
# 01/16/20 by Jianfa
# ------------------------------

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def isSubsequence(s, t):
            # check if string t is subsequence of string s
            i = 0
            for c in s:
                if i != len(t) and t[i] == c:
                    i += 1
            
            return i == len(t)
        
        length = 0
        res = "" # candidate longest string
        for string in d:
            if isSubsequence(s, string):
                if len(string) > length or len(string) == length and string < res:
                    length = len(string)
                    res = string
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Though 522 is not a good problem, it provides me the idea of checking subsequence.
# Check every string in dictionary to see if it's the subsequence of string s, then update
# the candidate string accoring to length and lexicographical order.