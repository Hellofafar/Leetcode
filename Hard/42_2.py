# ------------------------------
# 42. Trapping Rain Water
# 
# Description:
# Given n non-negative integers representing an elevation map where the width of each 
# bar is 1, compute how much water it is able to trap after raining.
# (see picture on the website)
# 
# Example:
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
# Version: 2.0
# 11/09/19 by Jianfa
# ------------------------------

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        current = 0
        stack = []
        while current < len(height):
            while stack and height[current] > height[stack[-1]]:
                last = stack.pop()
                if not stack:
                    # if stack is empty after popping last out
                    break
                distance = current - stack[-1] - 1 # get horizontal distance between current and left bar of the last
                height_diff = min(height[stack[-1]], height[current]) - height[last] # get the height distance between a lower bar and height[last]
                res += distance * height_diff
            
            stack.append(current)
            current += 1
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Stack solution from https://leetcode.com/problems/trapping-rain-water/solution/
# More concise than mine. It leverage the status of stack. If stack is empty, that means
# current bar is the only higher bar than last bar so far. Otherwise, there must be a
# left higher bar so that form a trap between it and current bar.
# Repeat this until there is no lower bar than current one.
# 
# O(n) time and O(n) space