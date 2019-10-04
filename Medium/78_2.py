# ------------------------------
# 78. Subsets
# 
# Description:
# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
# 
# For example,
# If nums = [1,2,3], a solution is:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
# 
# Version: 2.0
# 10/03/18 by Jianfa
# ------------------------------

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def backtrack(index, length):
            if len(temp) == length:
                res.append(list(temp))
            else:
                for i in range(index, len(nums)):
                    temp.append(nums[i])
                    backtrack(i+1, length)
                    temp.pop()
        
        for i in range(len(nums) + 1):
            # For all the lengths of possible subset
            backtrack(0, i)
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()
    nums = [1,3,5]
    test.subsets(nums)

# ------------------------------
# Summary:
# Easier to understand backtrack solution.