# ------------------------------
# 215. Kth Largest Element in an Array
# 
# Description:
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# Example 2:
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
# Version: 2.0
# 11/17/19 by Jianfa
# ------------------------------

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return heapq.heappop(nums)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Heap solution.
# Or use built-in func in heapq: heapq.nlargest(k, nums)[-1]
# 
# O(N * logN) time (for heapify)
# 
# If using heapq.nlargest() it's O(N * logk) time