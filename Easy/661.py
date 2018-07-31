# ------------------------------
# 661. Image Smoother
# 
# Description:
# Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.
# Example 1:
# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# 
# Note:
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].
# 
# Version: 1.0
# 07/30/18 by Jianfa
# ------------------------------

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if not M or not M[0]:
            return []
        
        R = len(M)
        C = len(M[0])
        res = []
        
        for i in range(len(M)):
            temp = []
            for j in range(len(M[0])):
                cell = 0
                count = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x >= 0 and x < R and y >= 0 and y < C:
                            cell += M[x][y]
                            count += 1
                
                cell = int(cell / count)
                temp.append(cell)
            
            res.append(temp)
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 