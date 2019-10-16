# ------------------------------
# 452. Minimum Number of Arrows to Burst Balloons
# 
# Description:
# There are a number of spherical balloons spread in two-dimensional space. For each balloon, 
# provided input is the start and end coordinates of the horizontal diameter. Since it's 
# horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the 
# diameter suffice. Start is always smaller than end. There will be at most 104 balloons.
# 
# An arrow can be shot up exactly vertically from different points along the x-axis. A balloon 
# with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to 
# the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. 
# The problem is to find the minimum number of arrows that must be shot to burst all balloons.
# 
# Example:
# Input:
# [[10,16], [2,8], [1,6], [7,12]]
# Output:
# 2
# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) 
# and another arrow at x = 11 (bursting the other two balloons).
# 
# Version: 1.0
# 10/15/19 by Jianfa
# ------------------------------

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return len(points)
        
        # Sort the points by the end position,
        # so that guarantee the next point's end coordinate is not less than current point's end coordinate
        points.sort(key=lambda x: x[1])
        
        count = 1
        overlap = points[0]
        for i in range(1, len(points)):
            if points[i][0] > overlap[1]:
                # require a new arrow
                count += 1
                overlap = points[i]
            
            elif points[i][0] > overlap[0]:
                # update overlap range that current arrow can shot balloon
                overlap[0] = points[i][0]
        
        return count

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Similar idea as meeting room II (253)
# difference is here is to find overlap as much as possible,
# but for meeting room is to find no overlap as much as possible