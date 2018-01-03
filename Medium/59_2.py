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
# Version: 2.0
# 01/03/18 by Jianfa
# ------------------------------

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        
        mat = []
        for i in range(n):
            mat.append([0 for i in range(n)])
        num = 0
        
        i, j = 0, -1
        row = n
        col = n
        while True:
            for c in range(col):
                j += 1
                num += 1
                mat[i][j] = num
            row -= 1
            if row == 0:
                break
                
            for r in range(row):
                i += 1
                num += 1
                mat[i][j] = num
            col -= 1
            if col == 0:
                break
                
            for c in range(col):
                j -= 1
                num += 1
                mat[i][j] = num
            row -= 1
            if row == 0:
                break
            
            for r in range(row):
                i -= 1
                num += 1
                mat[i][j] = num
            col -= 1
            if col == 0:
                break
        
        return mat

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Fill in the matrix one by one.
# Ref: sample 32 ms submission (python)