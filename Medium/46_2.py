# ------------------------------
# 46. Permutations
# 
# Description:
# Given a collection of distinct numbers, return all possible permutations.
# 
# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
# 
# Version: 2.0
# 10/03/17 by Jianfa
# ------------------------------

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        self.backtrack(nums, res, temp)
        return res
        
    def backtrack(self, nums, res, temp):
        if len(temp) == len(nums):
            res.append(list(temp))
            return
        
        for i in nums:
            if i not in temp:
                temp.append(i)
                self.backtrack(nums, res, temp)
                temp.pop()

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Easier to understand backtrack solution