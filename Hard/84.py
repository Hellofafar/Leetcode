# ------------------------------
# 84. Largest Rectangle in Histogram
# 
# Description:
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find 
# the area of largest rectangle in the histogram.
# 
# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.
# 
# Version: 1.0
# 01/27/18 by Jianfa
# ------------------------------

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        
        stack = []
        max_area = 0
        i = 0
        
        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            
            else:
                top_i = stack.pop()
                area_with_top = heights[top_i] * (i if not stack else i - stack[-1] - 1)
                
                if area_with_top > max_area:
                    max_area = area_with_top
            
        while len(stack) > 0:
            top_i = stack.pop()
            area_with_top = heights[top_i] * (i if not stack else i - stack[-1] - 1)
            
            if area_with_top > max_area:
                max_area = area_with_top
                
        return max_area
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow the idea from: https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
# The key point is to use a stack to record index of bar, when the stack is empty or the bar is greater than
# previous bar. If current bar is lower than the top bar, calculate the area including top bar (current bar is
# not included).