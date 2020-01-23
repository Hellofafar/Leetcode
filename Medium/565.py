# ------------------------------
# 565. Array Nesting
# 
# Description:
# A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return 
# the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to 
# the rule below.
# 
# Suppose the first element in S starts with the selection of element A[i] of index = i, 
# the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop 
# adding right before a duplicate element occurs in S.
# 
# Example 1:
# 
# Input: A = [5,4,0,3,1,6,2]
# Output: 4
# Explanation: 
# A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.
# 
# One of the longest S[K]:
# S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
# 
# Note:
# 
# N is an integer within the range [1, 20,000].
# The elements of A are all distinct.
# Each element of A is an integer within the range [0, N-1].
# 
# Version: 1.0
# 01/22/20 by Jianfa
# ------------------------------

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        size = len(nums)
        longest = 0
        for i in range(size):
            if nums[i] != -1:
                length = 0
                start = i
                while nums[start] != -1:
                    length += 1
                    temp = nums[start]
                    nums[start] = -1
                    start = temp
                longest = max(longest, length)
        
        return longest

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# At first I used a visited set to track the numbers visited, but that would cost space
# After reading the solution, I updated the corresponding index of number to -1 in order
# to record which number was visited.
# 
# O(n) time, O(1) space