# ------------------------------
# 120. Triangle
# 
# Description:
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
# 
# Version: 1.0
# 08/14/18 by Jianfa
# ------------------------------

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or not triangle[0]:
            return 0
        
        for i in range(len(triangle) - 1)[::-1]:
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        
        return triangle[0][0]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 