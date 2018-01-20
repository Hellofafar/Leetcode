# ------------------------------
# 73. Set Matrix Zeroes
# 
# Description:
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
# 
# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
# 
# Version: 1.0
# 01/19/18 by Jianfa
# ------------------------------

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(m)[::-1]:
            for j in range(1,n)[::-1]:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow the idea from: https://discuss.leetcode.com/topic/5056/any-shorter-o-1-space-solution
# O(1) space complexity