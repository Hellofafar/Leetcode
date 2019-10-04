# ------------------------------
# 47. Permutations II
# 
# Description:
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# 
# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
# 
# Version: 2.0
# 10/03/19 by Jianfa
# ------------------------------

from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        self.backtrack(nums, res, temp, Counter(nums))
        return res
    
    def backtrack(self, nums, res, temp, counter):
        if len(temp) == len(nums):
            res.append(list(temp))
        
        for i in counter:  # Don't pick duplicates
            if counter[i] > 0:
                temp.append(i)
                counter[i] -= 1
                self.backtrack(nums, res, temp, counter)
                counter[i] += 1
                temp.pop()

if __name__ == "__main__":
    test = Solution()
    nums = [1,1,2]

    print(test.permute(nums))

# ------------------------------
# Summary:
# Easier to understand backtrack solution.
# Key point is to use Counter to avoid duplicate number.
# Idea from: https://leetcode.com/problems/permutations-ii/discuss/18602/9-line-python-solution-with-1-line-to-handle-duplication-beat-99-of-others-%3A-)