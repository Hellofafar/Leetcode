# ------------------------------
# 39. Combination Sum
# 
# Description:
# Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations 
# in C where the candidate numbers sums to T.
# The same repeated number may be chosen from C unlimited number of times.
# 
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7, 
# A solution set is: 
# [
#   [7],
#   [2, 2, 3]
# ]
# 
# Version: 1.0
# 11/01/17 by Jianfa
# ------------------------------

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        temp = []
        candidates.sort()
        start = 0
        self.backtrack(result, temp, candidates, target, start)
        return result
        
    def backtrack(self, result, comb, candidates, target, start):
        if target == 0:
            comb_res = [x for x in comb]
            result.append(comb_res)
        
        elif target < 0:
            return
        
        else:
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                new_target = target - candidates[i]
                self.backtrack(result, comb, candidates, new_target, i)
                comb.pop()


# Used for test
if __name__ == "__main__":
    test = Solution()
    candidates = [2, 3]
    target = 5

    print(test.combinationSum(candidates, target))

# ------------------------------
# Summary:
# Backtrack problem.
# I spent long time thinking ahout backtracking. 
# 1. A necessary key for success is to sort the candidates and add 
# a parameter "start" in backtrack function. With "start", there is no need to traverse the candidates from 
# start during backtracking.
# 2. It's important to saparate the situation, e.g. target == 0, target < 0 or target > 0
# 3. One of the trap in python is that, in the line 32, I at first wrote result.append(comb). However, comb
# is a reference in backtrack function that it may be modified, which will lead to the modification in result.
# Alternative solution is result.append(comb[:])