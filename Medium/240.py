# ------------------------------
# 240. Search a 2D Matrix II
# 
# Description:
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# 
# Example:
# Consider the following matrix:
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
# Given target = 20, return false.
# 
# Version: 1.0
# 09/26/18 by Jianfa
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
        
        rightMost = len(matrix[0]) - 1  # Range of right most
        bottomMost = len(matrix) - 1    # Range of bottom most
        
        i = j = 0  # Starting point
        while i <= bottomMost and j <= rightMost:
            if matrix[i][j] == target:
                return True
            
            elif matrix[i][j] > target:
                return False
            
            for m in range(i, bottomMost + 1):
                if matrix[m][j] == target:
                    return True
                
                elif matrix[m][j] > target:
                    bottomMost = m - 1
                    break
            
            for n in range(j, rightMost + 1):
                if matrix[i][n] == target:
                    return True
                
                elif matrix[i][n] > target:
                    rightMost = n - 1
                    break
                    
            i += 1
            j += 1
        
        return False

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Divide and conquer solution. Complexity is O(mn)
# Another much better solution would be start from the top right.
# If the target is less than current number, the target cannot be in an entire column;
# if the target is greater than current number, the targer cannot be in an entire row.
# The complexity will be O(m + n)