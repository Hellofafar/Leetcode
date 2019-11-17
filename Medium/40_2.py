# ------------------------------
# 40. Combination Sum II
# 
# Description:
# Given a collection of candidate numbers (candidates) and a target number (target), find 
# all unique combinations in candidates where the candidate numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note:
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# 
# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]
# 
# Version: 2.0
# 11/15/19 by Jianfa
# ------------------------------

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        candidates.sort()
        res = []
        
        def backtrack(curr, index, target, start):
            # start is the index of where starting to check in this round
            
            if target == 0:
                res.append(curr[:])
            else:
                while index < len(candidates) and candidates[index] <= target:
                    if index > start and candidates[index] == candidates[index-1]:
                        # skip this value to avoid duplicate check
                        index += 1
                        continue
                    curr.append(candidates[index])
                    backtrack(curr, index+1, target - candidates[index], index+1)
                    curr.pop()
                    index += 1
        
        backtrack([], 0, target, 0)
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Met similar problem in Microsoft onsite interview. Difference is duplicate may exist in
# this problem so have to avoid it.
# 
# More concose solution than 40.py.
# 
# O(2^n) time