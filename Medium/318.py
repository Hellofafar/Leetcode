# ------------------------------
# 318. Maximum Product of Word Lengths
# 
# Description:
# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words 
# do not share common letters. You may assume that each word will contain only lower case letters. If no such 
# two words exist, return 0.
# 
# Example 1:
# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16 
# Explanation: The two words can be "abcw", "xtfn".
# 
# Example 2:
# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4 
# Explanation: The two words can be "ab", "cd".
# 
# Example 3:
# Input: ["a","aa","aaa","aaaa"]
# Output: 0 
# Explanation: No such pair of words.
# 
# Version: 1.0
# 09/26/19 by Jianfa
# ------------------------------

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if not words:
            return 0
        
        d = {}
        for w in words:
            key = 0
            for c in set(w):
                key |= 1 << (ord(c) - 97)
            # Get the size of longest word having same key 
            d[key] = max(d.get(key, 0), len(w))
        
        # x and y should share share no common letters
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])

# Used for testing
if __name__ == "__main__":
    test = Solution()
    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    words = ["a","aa","aaa","aaaa"]

# ------------------------------
# Summary:
# Get idea from: https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/76970/Python-solution-beats-99.67
# Use value 1 << x to represent characters existing in the word, which save the space nad calculation time.
# Calculate the length product if two value's bitwise AND operation is zero.