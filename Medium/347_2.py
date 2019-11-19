# ------------------------------
# 347. Top K Frequent Elements
# 
# Description:
# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
# Example 2:
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# Note:
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# 
# Version: 2.0
# 11/18/19 by Jianfa
# ------------------------------

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for key in counter:
            if len(heap) < k:
                heapq.heappush(heap, (counter[key], key))
            elif heap[0][0] < counter[key]:
                heapq.heapreplace(heap, (counter[key], key))
        
        res = []
        for item in heap:
            res.append(item[1])
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Heap solution
# 
# During for loop, O(N * logK) time
# last for loop, O(N) or O(K * logK) strictly
# O(N) space for hashmap