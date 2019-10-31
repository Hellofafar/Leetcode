# ------------------------------
# 1170. Compare Strings by Frequency of the Smallest Character
# 
# Description:
# Let's define a function f(s) over a non-empty string s, which calculates the frequency 
# of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the 
# smallest character is "c" and its frequency is 2.
# 
# Now, given string arrays queries and words, return an integer array answer, where each 
# answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.
# 
# Example 1:
# Input: queries = ["cbd"], words = ["zaaaz"]
# Output: [1]
# Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
# 
# Example 2:
# Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# Output: [1,2]
# Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") 
# and f("aaaa") are both > f("cc").
# 
# Constraints:
# 1 <= queries.length <= 2000
# 1 <= words.length <= 2000
# 1 <= queries[i].length, words[i].length <= 10
# queries[i][j], words[i][j] are English lowercase letters.
# 
# Version: 1.0
# 10/30/19 by Jianfa
# ------------------------------

from collections import Counter
from bisect import bisect

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        res = []
        wFreq = []
        for w in words:
            # get a sorted frequency number list from words
            wFreq.append(self.helper(w))
        wFreq.sort()
        size = len(wFreq)
        
        for q in queries:
            freq = self.helper(q)
            # find the index of freq in wFreq, then get how many numbers are larger than freq
            res.append(size - bisect(wFreq, freq))
        
        return res
    
    def helper(self, string):
        counter = Counter(string)
        return counter[min(counter.keys())]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Binary search solution.
# O(m * (x + logn)) + O(n * (y + logn)), m is len(queries), n is len(words), x is max(len(query)), y is max(len(word))
# O(m + n)