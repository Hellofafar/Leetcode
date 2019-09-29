# ------------------------------
# 347. Top K Frequent Elements
# 
# Description:
# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# 
# Version: 1.0
# 09/28/19 by Jianfa
# ------------------------------

import heapq
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        heap = []
        return heapq.nlargest(k, count.keys(), count.get)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/top-k-frequent-elements/solution/
# Learn to use heapq.nlargest, which is equivalent to: sorted(iterable, key=key, reverse=True)[:n].