# ------------------------------
# 447. Number of Boomerangs
# 
# Description:
# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
# Example:
# Input:
# [[0,0],[1,0],[2,0]]
# Output:
# 2
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
# 
# Version: 1.0
# 07/05/18 by Jianfa
# ------------------------------

from collections import defaultdict

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        distmap = defaultdict(int)
        
        for i in points:
            for j in points:
                dist = self.calDist(i, j)
                distmap[dist] += 1
            
            for v in distmap.values():
                res += v * (v - 1)
            
            distmap.clear()
        
        return res
                
    
    def calDist(self, i, j):
        return pow(i[0] - j[0], 2) + pow(i[1] - j[1], 2)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow the idea from https://leetcode.com/problems/number-of-boomerangs/discuss/92861/Clean-java-solution:-O(n2)-166ms
# O(n^2) solution