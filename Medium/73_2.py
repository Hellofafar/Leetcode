# ------------------------------
# 73. Set Matrix Zeroes
# 
# Description:
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
# 
# Example 1:
# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# 
# Example 2:
# Input: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# 
# Follow up:
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
# 
# Version: 2.0
# 11/09/19 by Jianfa
# ------------------------------

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # use matrix[0][0] to indicate the first row is marked
        # so use an extra variable col0 to indicate the first column has been marked
        col0 = False
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True
            
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                # check from row 1 column 1
                # if start from row1, it may set some matrix[0][j] wrongly, which means column j should be marked 0 but not
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(1, n):
                matrix[0][j] = 0
        
        if col0:
            # if the column 0 is marked, then set all items to 0
            for i in range(m):
                matrix[i][0] = 0

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from https://leetcode.com/problems/set-matrix-zeroes/solution/ Approach 3
# 
# O(MN) time O(1) space