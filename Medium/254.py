# ------------------------------
# 254. Factor Combinations
# 
# Description:
# Numbers can be regarded as product of its factors. For example,
# 
# 8 = 2 x 2 x 2;
#   = 2 x 4.
# Write a function that takes an integer n and return all possible combinations of its factors.
# 
# Note:
# 
# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.
# 
# Example 1:
# 
# Input: 1
# Output: []
# 
# Example 2:
# 
# Input: 37
# Output:[]
# 
# Example 3:
# 
# Input: 12
# Output:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
# 
# Example 4:
# 
# Input: 32
# Output:
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]
# 
# Version: 1.0
# 11/26/19 by Jianfa
# ------------------------------

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = self.helper(n, 2)
        res.remove([n]) # remove the last [n] appended in the helper function
        return res
            
    def helper(self, n, start):
        # n is the number to divide
        # start is the smallest factor to start checking
        ret = []
        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                for comb in self.helper(n // i, i):
                    ret.append([i] + comb) # current factor is i, so start factor should at least be i
        
        ret.append([n])
        return ret

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Recursive solution.
# Remember to remove [n] at the end.