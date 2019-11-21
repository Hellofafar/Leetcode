# ------------------------------
# 554. Brick Wall
# 
# Description:
# There is a brick wall in front of you. The wall is rectangular and has several rows of 
# bricks. The bricks have the same height but different width. You want to draw a vertical 
# line from the top to the bottom and cross the least bricks.
# 
# The brick wall is represented by a list of rows. Each row is a list of integers representing 
# the width of each brick in this row from left to right.
# 
# If your line go through the edge of a brick, then the brick is not considered as crossed. 
# You need to find out how to draw the line to cross the least bricks and return the number 
# of crossed bricks.
# 
# You cannot draw a line just along one of the two vertical edges of the wall, in which case 
# the line will obviously cross no bricks.
# 
# Example:
# Input: [[1,2,2,1],
#         [3,1,2],
#         [1,3,2],
#         [2,4],
#         [3,1,2],
#         [1,3,1,1]]
# 
# Output: 2
# 
# Version: 1.0
# 11/20/19 by Jianfa
# ------------------------------

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall or not wall[0]:
            return 0
        
        # mapping of edge position -> count
        positionMap = collections.defaultdict(int)
        for w in wall:
            pos = 0
            for i in range(len(w) - 1):
                # for every brick except the last brick on the row, get the right edge of it and add 1 to map[edge_position]
                pos += w[i]
                positionMap[pos] += 1
        
        if not positionMap:
            return len(wall)
        return len(wall) - max(positionMap.values())

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/brick-wall/discuss/101728/I-DON'T-THINK-THERE-IS-A-BETTER-PERSON-THAN-ME-TO-ANSWER-THIS-QUESTION
# 
# It's easy to understand. Turn the problem to find an edge where it's the most common
# horizontal location, then it's the location to cross bricks.
# Using a map to store edge locations.
# 
# Take care edge cases: right edge of last brick shouldn't be counted since it's end of the wall
# Even if wall list is not null, the map could be null finally e.g. [[1],[1],[1]]
# 
# O(MN) time O(K) space, K is number of edges, worst case is MN