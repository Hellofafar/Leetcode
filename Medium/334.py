# ------------------------------
# 334. Increasing Triplet Subsequence
# 
# Description:
# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
# 
# Formally the function should:
# Return true if there exists i, j, k 
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.
# 
# Example 1:
# Input: [1,2,3,4,5]
# Output: true
# 
# Example 2:
# Input: [5,4,3,2,1]
# Output: false
# 
# Version: 1.0
# 09/27/19 by Jianfa
# ------------------------------

import sys

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = sys.maxsize
        large = sys.maxsize
        for n in nums:
            if n <= small:
                small = n
            elif n <= large:
                large = n
            else:
                return True
        
        return False

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/increasing-triplet-subsequence/discuss/79004/Concise-Java-solution-with-comments.
# Start with two largest values, as soon as we find a number bigger than both, while both have been updated, return true.