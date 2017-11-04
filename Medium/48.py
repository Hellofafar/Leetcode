# ------------------------------
# 48. Rotate Image
# 
# Description:
# You are given an n x n 2D matrix representing an image.
# 
# Rotate the image by 90 degrees (clockwise).
# 
# Note:
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT 
# allocate another 2D matrix and do the rotation.
# 
# Example 1:
# 
# Given input matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# 
# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# 
# Version: 1.0
# 11/03/17 by Jianfa
# ------------------------------

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    test = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]

    print(test.rotate(matrix))

# ------------------------------
# Summary:
# Follow the idea in discuss section. Use list.reverse() here.
# 
# a common method to solve the image rotation problems.
# 
# clockwise rotate
# first reverse up to down, then swap the symmetry 
# 1 2 3     7 8 9     7 4 1
# 4 5 6  => 4 5 6  => 8 5 2
# 7 8 9     1 2 3     9 6 3
# 
# anticlockwise rotate
# first reverse left to right, then swap the symmetry
# 1 2 3     3 2 1     3 6 9
# 4 5 6  => 6 5 4  => 2 5 8
# 7 8 9     9 8 7     1 4 7
