# ------------------------------
# 692. Top K Frequent Words
# 
# Description:
# Given a non-empty list of words, return the k most frequent elements.
# 
# Your answer should be sorted by frequency from highest to lowest. If two words have 
# the same frequency, then the word with the lower alphabetical order comes first.
# 
# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# 
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# 
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.
# 
# Version: 1.0
# 11/02/19 by Jianfa
# ------------------------------

from collections import Counter
import heapq
import functools

@functools.total_ordering
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word
    
    def __lt__(self, other): # it acheives that Element(2, "ac") < Element(2, "ab")
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        
        heap = [] # a heap to store elements
        for w, count in counter.items():
            heapq.heappush(heap, (Element(count, w), w))
            if len(heap) > k:
                # if heap has more than k elements, pop out the smallest one
                heapq.heappop(heap)
        
        res = []
        while heap:
            element = heapq.heappop(heap)
            res.append(element[1])
        
        return res[::-1]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/top-k-frequent-words/discuss/108348/Python-3-solution-with-O(nlogk)-and-O(n)
# I know how to use heap but I don't know how to change the order rule when using heap.
# About @functools.total_ordering: https://leetcode.com/problems/top-k-frequent-words/discuss/108348/Python-3-solution-with-O(nlogk)-and-O(n)
# 
# For your class, after defining one of __lt__(), __le__(), __gt__(), or __ge__(), AND 
# an __eq__() method, this class decorator supplies the rest.
# This is to simplify the effort involved in specifying all of the possible rich comparison operations.