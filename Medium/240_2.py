# ------------------------------
# 240. Search a 2D Matrix II
# 
# Description:
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix 
# has the following properties:
# 
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# 
# Example:
# Consider the following matrix:
# 
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
# 
# Given target = 20, return false.
# 
# Version: 2.0
# 11/12/19 by Jianfa
# ------------------------------

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        # start search from right top corner
        i = 0
        j = n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            
            elif matrix[i][j] > target:
                j -= 1
            
            else:
                i += 1
        
        return False

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Start searching from right top corner, can leverage the sorted feature
# 
# O(M + N) time O(1) space 