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
# Version: 1.0
# 01/20/18 by Jianfa
# ------------------------------

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            return []
        
        res = []
        currlist = []
        self.backtrack(n, k, currlist, 1, res)
        return res
        
    
    def backtrack(self, n, k, currlist, start, res):
        if len(currlist) == k:
            temp = [x for x in currlist]
            res.append(temp)
        
        elif n - start + 1 + len(currlist) < k:
            return
        
        else:
            for i in range(start, n+1):
                currlist.append(i)
                self.backtrack(n, k, currlist, i+1, res)
                currlist.pop()

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Backtrack solution.
# The tough point is you must clearly understand what every step is in the backtrack process.
# I didn't think quite clear at first, but finally I realized that there is a stack in the
# backtrack function. Check "else" part in backtrack(), there will be an append() before
# recursive backtrack, and a pop() after the recursive backtrack.