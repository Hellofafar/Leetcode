# ------------------------------
# 54. Spiral Matrix
# 
# Description:
# 
# Version: 1.0
# 11/18/17 by Jianfa
# ------------------------------

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        direction = [0, 1, 0, -1]
        
        if not matrix or not matrix[0]:
            return []
        
        x = 0
        y = 0
        start = 0
        xdirection = direction[start % 4]
        ydirection = direction[(start + 1) % 4]
        res = []
        while 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] != None:                      
            while 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] != None:
                res.append(matrix[x][y])
                matrix[x][y] = None
                x += xdirection
                y += ydirection

            print (x, y, xdirection, ydirection)
            x -= xdirection
            y -= ydirection
            start += 1
            xdirection = direction[start % 4]
            ydirection = direction[(start + 1) % 4]
            x += xdirection
            y += ydirection
        
        return res
        

# Used for testing
if __name__ == "__main__":
    test = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]

    print(test.spiralOrder(matrix))

# ------------------------------
# Summary:
# Find the boundary condition of change direction that either reach the length limit of matrix, or the next 
# item has been visited.
# Then change the direction by clockwise rotation (90 degree), which is implemented by directions list.
# [0, 1, 0, -1] every time pick up two neighbour integer to represent the moving direction of x and y.