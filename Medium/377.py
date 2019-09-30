# ------------------------------
# 377. Combination Sum IV
# 
# Description:
# Given an integer array with all positive numbers and no duplicates, find the number of 
# possible combinations that add up to a positive integer target.
# 
# Example:
# nums = [1, 2, 3]
# target = 4
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 
# Note that different sequences are counted as different combinations.
# Therefore the output is 7.
# 
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?
# 
# Version: 1.0
# 09/29/19 by Jianfa
# ------------------------------

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        comb = [-1 for _ in range(target+1)]
        return self.dp(comb, nums, target)
    
    def dp(self, comb: List[int], nums: List[int], target: int) -> int:
        if target == 0:
            return 1
        
        if comb[target] != -1:
            return comb[target]
        
        count = 0
        for n in nums:
            temp = target
            if target >= n:
                count += self.dp(comb, nums, target - n)
            
        comb[target] = count
        
        return count

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from: https://leetcode.com/problems/combination-sum-iv/discuss/85036/1ms-Java-DP-Solution-with-Detailed-Explanation
# I independently thought about the recursive solution but got TLE when number is large.
# The improvement of this idea is to use a list to store the intermediate results so we don't have to calculate same result
# again during dp process.