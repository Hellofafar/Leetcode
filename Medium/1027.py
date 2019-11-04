# ------------------------------
# 1027. Longest Arithmetic Sequence
# 
# Description:
# Given an array A of integers, return the length of the longest arithmetic subsequence in A.

# Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < 
# ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are all the 
# same value (for 0 <= i < B.length - 1).
# 
# Example 1:
# Input: [3,6,9,12]
# Output: 4
# Explanation: 
# The whole array is an arithmetic sequence with steps of length = 3.
# 
# Example 2:
# Input: [9,4,7,2,10]
# Output: 3
# Explanation: 
# The longest arithmetic subsequence is [4,7,10].
# 
# Example 3:
# Input: [20,1,15,3,10,5,8]
# Output: 4
# Explanation: 
# The longest arithmetic subsequence is [20,15,10,5].
# 
# Note:
# 2 <= A.length <= 2000
# 0 <= A[i] <= 10000
# 
# Version: 1.0
# 11/03/19 by Jianfa
# ------------------------------

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {} # dp[(index, diff)] is the length of longest arithmetic subsequence ending at index with difference diff
        
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1 # get((i, A[j] - A[i]), 1) the 1 is for the single element length
        
        return max(dp.values())

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DP solution from: https://leetcode.com/problems/longest-arithmetic-sequence/discuss/274611/JavaC%2B%2BPython-DP
# 
# O(N^2) time, O(N^2) space