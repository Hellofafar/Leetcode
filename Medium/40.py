# ------------------------------
# 40. Combination Sum II
# 
# Description:
# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where 
# the candidate numbers sums to T.
# Each number in C may only be used once in the combination.
# 
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
# A solution set is: 
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# 
# Version: 1.0
# 11/01/17 by Jianfa
# ------------------------------

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        comb = []
        start = 0
        candidates.sort()
        self.buildCombination(result, comb, candidates, target, start)
        return result
        
    def buildCombination(self, result, comb, candidates, target, start):
        if target == 0:
            result.append(comb[:])
        
        else:
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:  
                    # When there is duplicate, only the first one will be used for backtracking,
                    # because it will cover all situations
                    continue

                if candidates[i] > target:  # Here is for reducing numbers of checking (Compared to 39.py)
                    break
                else:
                    comb.append(candidates[i])
                    new_target = target - candidates[i]
                    self.buildCombination(result, comb, candidates, new_target, i + 1)  # i + 1 here, because every number can only used once
                    comb.pop()


# Used for test
if __name__ == "__main__":
    test = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8

    print(test.combinationSum2(candidates, target))

# ------------------------------
# Summary:
# Very similar to 39.py. The only difference is, in the collection there may be duplicate numbers and in combination,
# every number can only be used once.
# The details can see my comments.