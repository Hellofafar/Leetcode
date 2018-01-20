# ------------------------------
# 74. Search a 2D Matrix
# 
# Description:
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the 
# following properties:
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
# Consider the following matrix:
# 
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.
# 
# Version: 1.0
# 01/20/18 by Jianfa
# ------------------------------

class Solution(object):
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
        
        # Search the row
        low0 = 0
        high0 = m - 1
        
        if matrix[low0][0] > target or matrix[high0][n-1] < target:
            return False
        
        while low0 < high0 - 1:
            mid0 = (low0 + high0) / 2
            if matrix[mid0][0] < target:
                low0 = mid0
            
            elif matrix[mid0][0] > target:
                high0 = mid0 - 1
            
            else:
                return True
        
        if matrix[high0][0] <= target:
            mid0 = high0
        else:
            mid0 = low0
        
        low1 = 0
        high1 = n - 1

        if matrix[mid0][low1] > target or matrix[mid0][high1] < target:
            return False
        
        while low1 < high1:
            mid1 = (low1 + high1) / 2
            if matrix[mid0][mid1] < target:
                low1 = mid1 + 1
            
            elif matrix[mid0][mid1] > target:
                high1 = mid1 - 1
            
            else:
                return True
        
        mid1 = (low1 + high1) / 2
        if matrix[mid0][mid1] == target: # Last check in case no check during two while loop
            return True
        
        return False

# Used for testing
if __name__ == "__main__":
    test = Solution()
    matrix = [[1],[10]]
    target = 10
    print(test.searchMatrix(matrix, target))

# ------------------------------
# Summary:
# Binary search solution.
# Search for candidate row at first, then search by column.
# Take care of some edge case. For example when there are only two rows, the first while loop
# will be skipped. In that case, mid0 cannot be (low0 + high0) / 2, because the candidate may
# be row high0. So matrix[high0][0] should be checked to see if it greater than target value.