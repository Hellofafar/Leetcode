# ------------------------------
# 308. Range Sum Query 2D - Mutable
# 
# Version: 1.0
# 11/07/17 by Jianfa
# ------------------------------

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.matrix[row][col] = val
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        total = 0
        for i in range(row1, row2 + 1):
            total += sum(self.matrix[i][col1:col2 + 1])
        
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)


# ------------------------------
# Summary:
# I don't know exactly what this problem is.