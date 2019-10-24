# ------------------------------
# 478. Generate Random Point in a Circle
# 
# Description:
# Given the radius and x-y positions of the center of a circle, write a function randPoint 
# which generates a uniform random point in the circle.
# 
# Note:
# 
# input and output values are in floating-point.
# radius and x-y position of the center of the circle is passed into the class constructor.
# a point on the circumference of the circle is considered to be in the circle.
# randPoint returns a size 2 array containing x-position and y-position of the random point, 
# in that order.
# 
# Example 1:
# Input: 
# ["Solution","randPoint","randPoint","randPoint"]
# [[1,0,0],[],[],[]]
# Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
# 
# Example 2:
# Input: 
# ["Solution","randPoint","randPoint","randPoint"]
# [[10,5,-7.5],[],[],[]]
# Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
# Explanation of Input Syntax:
# 
# The input is two lists: the subroutines called and their arguments. Solution's constructor 
# has three arguments, the radius, x-position of the center, and y-position of the center of 
# the circle. randPoint has no arguments. Arguments are always wrapped with a list, even if 
# there aren't any.
# 
# Version: 1.0
# 10/22/19 by Jianfa
# ------------------------------

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x_min, self.x_max = x_center - radius, x_center + radius
        self.y_min, self.y_max = y_center - radius, y_center + radius
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        while True:
            x, y = random.uniform(self.x_min, self.x_max), random.uniform(self.y_min, self.y_max)
            if pow(x - self.x_center, 2) + pow(y - self.y_center, 2) <= pow(self.radius, 2):
                return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Very easy to understand solution from https://leetcode.com/problems/generate-random-point-in-a-circle/discuss/154092/Very-simple-Python-solution
# Try to get random point within the square. If it's within the circle then return.
# The other solution using Math.sqrt(): https://leetcode.com/problems/generate-random-point-in-a-circle/discuss/155650/Explanation-with-Graphs-why-using-Math.sqrt()