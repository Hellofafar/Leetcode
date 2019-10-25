# ------------------------------
# 491. Increasing Subsequences
# 
# Description:
# Given an integer array, your task is to find all the different possible increasing subsequences 
# of the given array, and the length of an increasing subsequence should be at least 2.
# 
# Example:
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# 
# Note:
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
# 
# Version: 1.0
# 10/24/19 by Jianfa
# ------------------------------

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        self.helper(temp, res, 0, nums)
        return res
    
    def helper(self, temp, res, index, nums):
        if len(temp) > 1:
            res.append(list(temp))
        
        seen = set()  # store the elements that has been used in this round to avoid duplicate
        for i in range(index, len(nums)):
            n = nums[i]
            if n in seen:
                continue
            if len(temp) == 0 or n >= temp[-1]:
                seen.add(n)
                temp.append(n)
                self.helper(temp, res, i+1, nums)
                temp.pop()

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from https://leetcode.com/problems/increasing-subsequences/discuss/97147/Java-solution-beats-100