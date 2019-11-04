# ------------------------------
# 767. Reorganize String
# 
# Description:
# Given a string S, check if the letters can be rearranged so that two characters that are 
# adjacent to each other are not the same.
# 
# If possible, output any possible result.  If not possible, return the empty string.
# 
# Example 1:
# Input: S = "aab"
# Output: "aba"
# 
# Example 2:
# Input: S = "aaab"
# Output: ""
# 
# Note:
# S will consist of lowercase letters and have length in range [1, 500].
# 
# Version: 1.0
# 11/03/19 by Jianfa
# ------------------------------

from collections import defaultdict
import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        counter = defaultdict(int)
        for c in S:
            counter[c] += 1
            if counter[c] > (len(S) + 1) // 2:
                # if more than half of the total length, impossible to rearrange
                return ""
        
        charHeap = []
        # charHeap is a heap to store pairs of (-count, char)
        # Greedy: to fetch char of max count as next char in the result. Since heapq implements the min heap, make count to be negative to order in descending
        for c in counter:
            heapq.heappush(charHeap, [-counter[c], c])
        
        res = ""
        while charHeap:
            first = heapq.heappop(charHeap)
            if not res or first[1] != res[-1]:
                res += first[1]
                first[0] += 1 # first[0] is negative here, so add 1 actually means count minus 1
                if first[0] != 0:
                    heapq.heappush(charHeap, first)
            else:
                second = heapq.heappop(charHeap)
                res += second[1]
                second[0] += 1
                if second[0] != 0:
                    heapq.heappush(charHeap, second)
                heapq.heappush(charHeap, first) # char in first is not inserted, push first back to the heap
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Heap solution from: https://leetcode.com/problems/reorganize-string/discuss/113440/Java-solution-PriorityQueue
# Use a heap to store pairs (-count, char). count is negative here because want to implement
# a max heap.
# Then alternate placing the most common letters.
# 
# O(N * logK) time, N is length of S and K is unique char number
# O(K) space