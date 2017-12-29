# ------------------------------
# 59. Spiral Matrix II
# 
# Description:
# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
# For example,
# Given n = 3,
# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
# 
# Version: 1.0
# 12/29/17 by Jianfa
# ------------------------------

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A, lo = [], n*n+1
        print("A:", A)
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [range(lo, hi)] + zip(*A[::-1])
            print([range(lo, hi)], A)
        return A
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Ref: https://leetcode.com/problems/spiral-matrix-ii/discuss/22282