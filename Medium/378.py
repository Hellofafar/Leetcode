# ------------------------------
# 378. Kth Smallest Element in a Sorted Matrix
# 
# Description:
# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
# 
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
# 
# Example:
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
# return 13.
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n2.
# 
# Version: 1.0
# 09/30/19 by Jianfa
# ------------------------------

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return
        
        queue = []
        
        def heapPush(i, j):
            if i < len(matrix) and j < len(matrix[0]):
                heapq.heappush(queue, (matrix[i][j], i, j))
        
        heapPush(0, 0)
        while queue and k > 0:
            num, i, j = heapq.heappop(queue)
            heapPush(i, j+1)
            if j == 0:
                heapPush(i+1, 0)
            k -= 1
            
        return num

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Same idea as problem 373.
# O(klogk) time complexity