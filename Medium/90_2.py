# ------------------------------
# 90. Subsets II
# 
# Description:
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power 
# set).
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
# 
# Version: 2.0
# 10/03/19 by Jianfa
# ------------------------------

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        nums.sort() # Sorting is necessary here
        def backtrack(start):
            res.append(list(temp))
            
            for i in range(start, len(nums)):
                if i > start and nums[i-1] == nums[i]: # avoid pick duplicates
                    continue

                temp.append(nums[i])
                backtrack(i+1)
                temp.pop()
        
        backtrack(0)
        return res          

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Easier to understand backtrack solution.