# ------------------------------
# 223. Rectangle Area
# 
# Description:
# Find the total area covered by two rectilinear rectangles in a 2D plane.
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
# 
# Example:
# Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
# Output: 45
# Note:
# Assume that the total area is never beyond the maximum possible value of int.
# 
# Version: 1.0
# 09/19/18 by Jianfa
# ------------------------------

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        left = max(A, E)                # left coordinate of overlap area (if exists)
        right = max(min(C, G), left)    # right coordinate. If no overlap, then right == left (because left >= min(C, G))
        top = min(D, H)
        bottom = min(max(B, F), top)
        
        return (C - A) * (D - B) + (G - E) * (H - F) - (right - left) * (top - bottom)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow idea from https://leetcode.com/problems/rectangle-area/discuss/62149/Just-another-short-way