# ------------------------------
# 300. Longest Increasing Subsequence
# 
# Description:
# Given an unsorted array of integers, find the length of longest increasing subsequence.
# 
# Example:
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
# 
# Note:
# 
# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# 
# Version: 2.0
# 11/13/19 by Jianfa
# ------------------------------

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums) # tail[i] smallest tail number of LIS with length i + 1. NOTE: tail number is the largest number in an increasing subsequence
        
        size = 0
        for x in nums:
            i = 0 # length of LIS
            j = size # current longest length
            while i != j:
                # i and j is like low and high in binary search
                mid = (i + j) // 2
                if x > tails[mid]:
                    # x > the largest number of at least one increasing subsequence with length mid + 1
                    i = mid + 1
                else:
                    # x <= the smallest tail number of LIS with length mid + 1
                    j = mid
            
            tails[i] = x # update tail[i] to x because x is the new smallest tail number
            size = max(i+1, size)
        
        return size

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
# 
# O(N * logN) time O(N) space