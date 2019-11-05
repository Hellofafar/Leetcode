# ------------------------------
# 836. Rectangle Overlap
# 
# Description:
# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates 
# of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.
# 
# Two rectangles overlap if the area of their intersection is positive.  To be clear, two 
# rectangles that only touch at the corner or edges do not overlap.
# 
# Given two (axis-aligned) rectangles, return whether they overlap.
# 
# Example 1:
# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
# 
# Example 2:
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
# 
# Notes:
# Both rectangles rec1 and rec2 are lists of 4 integers.
# All coordinates in rectangles will be between -10^9 and 10^9.
# 
# Version: 1.0
# 11/04/19 by Jianfa
# ------------------------------

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/rectangle-overlap/discuss/132340/C%2B%2BJavaPython-1-line-Solution-1D-to-2D
# From 1D to 2D:
# for 1D, if two segments (left1, right1), (left2, right2) overlap, then left1 < right2 && left2 < right1
# 
# O(1) time