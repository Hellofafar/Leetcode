# ------------------------------
# 77. Combinations
# 
# Description:
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# 
# For example,
# If n = 4 and k = 2, a solution is:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# 
# Version: 2.0
# 10/03/19 by Jianfa
# ------------------------------

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = []
        def backtrack(num):
            if len(temp) == k:
                res.append(list(temp))
            else:
                for i in range(num, n+1):
                    temp.append(i)
                    backtrack(i+1)
                    temp.pop()
        backtrack(1)
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Easier to understand backtrack solution.