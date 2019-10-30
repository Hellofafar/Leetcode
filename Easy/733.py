# ------------------------------
# 733. Flood Fill
# 
# Description:
# An image is represented by a 2-D array of integers, each integer representing the pixel 
# value of the image (from 0 to 65535).
# 
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood 
# fill, and a pixel value newColor, "flood fill" the image.
# 
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 
# 4-directionally to the starting pixel of the same color as the starting pixel, plus any 
# pixels connected 4-directionally to those pixels (also with the same color as the starting 
# pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
# 
# At the end, return the modified image.
# 
# Example 1:
# Input: 
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# 
# Explanation: 
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.
# 
# Note:
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
# The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
# 
# Version: 1.0
# 10/29/19 by Jianfa
# ------------------------------

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        queue = collections.deque()
        queue.append((sr, sc))
        
        dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        visited = set() # visited is a set to avoid duplicate searching, especially when newColor is oldColor
        visited.add((sr, sc))
        while queue:
            cur = queue.popleft()
            for d in dirs:
                r = cur[0] + d[0]
                c = cur[1] + d[1]
                if 0 <= r < m and 0 <= c < n and (r, c) not in visited and image[r][c] == oldColor:
                    # update the color and append this coordinate to the queue
                    image[r][c] = newColor
                    queue.append((r, c))
                    visited.add((r, c))
                    
        return image

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# BFS solution
# 
# O(m * n) time, O(m * n) space