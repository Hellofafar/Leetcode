# ------------------------------
# 149. Max Points on a Line
# 
# Description:
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
# 
# Example 1:
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
# 
# Example 2:
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
# 
# Version: 1.0
# 10/04/19 by Jianfa
# ------------------------------

from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        res = 0
        for i in range(len(points)):
            lineMax = 0
            slopeDict = defaultdict(int)
            overlap = 0
            for j in range(i+1, len(points)):
                x = points[j][0] - points[i][0]
                y = points[j][1] - points[i][1]
                if x == 0 and y == 0:
                    # two points overlap
                    overlap += 1
                    continue
                gcd = self.generateGCD(x, y)
                x //= gcd
                y //= gcd
                slope = str(y) + '/' + str(x) # Use string to store slope value
                slopeDict[slope] += 1
            
            if slopeDict:
                # Get the max number of points that lie on the same line which point i lies on
                lineMax = max(slopeDict.values())
            # When count the total number, overlap points should be considered
            res = max(res, lineMax + overlap + 1)
        
        return res
                
    def generateGCD(self, x, y):
        if y == 0:
            return x
        
        return self.generateGCD(y, x%y)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# O(N^2) solution from https://leetcode.com/problems/max-points-on-a-line/discuss/47113/A-java-solution-with-notes/46933
# One key point is to calculate the slope of two points, with the help of GCD, and store the slope result in a string