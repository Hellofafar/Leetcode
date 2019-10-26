# ------------------------------
# 497. Random Point in Non-overlapping Rectangles
# 
# Description:
# Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which 
# randomly and uniformily picks an integer point in the space covered by the rectangles.
# 
# Note:
# 
# An integer point is a point that has integer coordinates. 
# A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
# ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the 
# bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
# length and width of each rectangle does not exceed 2000.
# 1 <= rects.length <= 100
# pick return a point as an array of integer coordinates [p_x, p_y]
# pick is called at most 10000 times.
# 
# Example 1:
# Input: 
# ["Solution","pick","pick","pick"]
# [[[[1,1,5,5]]],[],[],[]]
# Output: 
# [null,[4,1],[4,1],[3,3]]
# 
# Example 2:
# Input: 
# ["Solution","pick","pick","pick","pick","pick"]
# [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
# Output: 
# [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
# Explanation of Input Syntax:
# 
# The input is two lists: the subroutines called and their arguments. Solution's constructor 
# has one argument, the array of rectangles rects. pick has no arguments. Arguments are always 
# wrapped with a list, even if there aren't any.
# 
# Version: 1.0
# 10/25/19 by Jianfa
# ------------------------------

class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.range = [0] # Add 0 at first is to make pick() easier
        self.summ = 0
        for rect in rects:
            self.summ += (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1) # Keep adding new result to make a new range
            self.range.append(self.summ)

    def pick(self):
        """
        :rtype: List[int]
        """
        n = random.randint(0, self.summ - 1)
        i = bisect.bisect(self.range, n)
        rect = self.rects[i-1] # A 0 is at the begining of self.range, so i will be starting 1, then i - 1 is the correct index of rect
        n -= self.range[i-1]   # Here is the reason why a 0 should be added at the begining of self.range
        x = rect[0] + n % (rect[2] - rect[0] + 1)
        y = rect[1] + n / (rect[2] - rect[0] + 1)
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/discuss/154147/Python-weighted-probability-solution/160274
# First populate the sum of each rectangle to a range list, then randomly pick a number 
# from this range.
# Manage to get x, y from just one-time random
# 
# O(n) time, O(n) space