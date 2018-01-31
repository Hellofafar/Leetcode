# ------------------------------
# 85. Maximal Rectangle
# 
# Description:
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return 
# its area.
# 
# For example, given the following matrix:
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 6.
# 
# Version: 1.0
# 01/30/18 by Jianfa
# ------------------------------

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        left = [0 for i in range(n)]
        right = [n for i in range(n)]
        height = [0 for i in range(n)]
        maxA = 0
        
        for i in range(m):
            curr_left = 0
            curr_right = n
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
                    
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], curr_left)
                else:
                    left[j] = 0
                    curr_left = j + 1
            
            for j in range(n)[::-1]:
                if matrix[i][j] == '1':
                    right[j] = min(right[j], curr_right)
                else:
                    right[j] = n
                    curr_right = j
            
            for j in range(n):
                maxA = max(maxA, (right[j] - left[j]) * height[j])
        
        return maxA

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Very very smart dynamic programming idea from: https://leetcode.com/problems/maximal-rectangle/discuss/29054
# Use left, right, and height to calculate the largest area for row i and column j.