# ------------------------------
# 42. Trapping Rain Water
# 
# Description:
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# (see picture on the website)
# 
# Example:
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
# Version: 1.0
# 10/20/19 by Jianfa
# ------------------------------

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        bars = []  # stack to store the height of each bar
        altitude = 0  # current altitude of the trap in order to calculate the filling water height
        count = 0
        for i, h in enumerate(height):
            if h == 0:
                altitude = 0
            else:
                while bars:
                    top = bars[-1] # top = (index, height)
                    if top[1] > h:
                        # current top bar of the stack is higher than h
                        count += (i - top[0] - 1) * (h - altitude)
                        break
                    else:
                        count += (i - top[0] - 1) * (top[1] - altitude)
                        altitude = top[1]  # update altitude after filling water
                        bars.pop()
                
                bars.append((i, h))
                altitude = h  # update altitude to latest bar height
        
        return count

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Stack solution.
# Use a variable to record current altitude after checking new height and filling water 
# every time
# For stack, if the top bar is lower or equal to incoming bar, calculate the filling 
# water amount between two bars then pop it out
# if the top bar is higher, also calculate the filling water amount between two bars 
# but not pop it out
# push the incoming bar into stack and update altitude
#
# O(n) time and O(n) space