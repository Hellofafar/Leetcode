# ------------------------------
# 216. Combination Sum III
# 
# Description:
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
# Note:
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# 
# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# 
# Version: 1.0
# 09/06/18 by Jianfa
# ------------------------------

class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        subset = []
        self.backtrack(k, n, 1, subset, res)
        
        return res
    
    def backtrack(self, k, n, i, subset, res):
        if k == 0:
            if n == 0:
                temp = [num for num in subset]
                res.append(temp)
            return
        
        for x in range(i, 10):
            if x <= n:
                subset.append(x)
                self.backtrack(k-1, n-x, x+1, subset, res)
                subset.pop()
            
            else:
                break

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Backtrack solution.