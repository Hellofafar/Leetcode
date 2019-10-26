# ------------------------------
# 498. Diagonal Traverse
# 
# Description:
# Given a matrix of M x N elements (M rows, N columns), return all elements of the 
# matrix in diagonal order as shown in the below image.
# 
# Example:
# 
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 
# Output:  [1,2,4,7,5,3,6,8,9]
# Note:
# The total number of elements of the given matrix will not exceed 10,000.
# 
# Version: 1.0
# 10/25/19 by Jianfa
# ------------------------------

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        
        res = [matrix[0][0]]
        diag = True # from bottom left to top right
        prev = [0, 0]
        while not (prev[0] == m-1 and prev[1] == n-1):
            if diag:
                if prev[0] - 1 >= 0 and prev[1] + 1 < n:
                    prev = [prev[0] - 1, prev[1] + 1]
                elif prev[0] - 1 < 0:
                    if prev[1] + 1 < n:
                        # At the top borderline
                        prev = [0, prev[1] + 1]
                    else:
                        # At the top right corner
                        prev = [1, n-1]
                    diag = not diag
                elif prev[1] + 1 >= n:
                    # At the right borderline
                    prev = [prev[0] + 1, n-1]
                    diag = not diag
            else:
                if prev[0] + 1 < m and prev[1] - 1 >= 0:
                    prev = [prev[0] + 1, prev[1] - 1]
                elif prev[1] - 1 < 0:
                    if prev[0] + 1 < m:
                        # At the left borderline
                        prev = [prev[0] + 1, 0]
                    else:
                        # At the bottom left corner
                        prev = [m-1, 1]
                    diag = not diag
                elif prev[0] + 1 >= m:
                    prev = [m-1, prev[1] + 1]
                    diag = not diag
            
            res.append(matrix[prev[0]][prev[1]])
        
        return res
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Use a bool value diag to indicate whether it's to-top-right traverse or to-bottom-left traverse
# Take care of the borderline cases
# Another idea that not using the boolean is decide the direction by (i + j) % 2, if it's 0 then 
# it's moving up, otherwise moving down
# O(m * n) time, O(1) space
# 