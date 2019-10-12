# ------------------------------
# 435. Non-overlapping Intervals
# 
# Description:
# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# 
# Example 1:
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
# 
# Example 2:
# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
# 
# Example 3:
# Input: [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
# 
# Note:
# You may assume the interval's end point is always bigger than its start point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
# 
# Version: 1.0
# 10/11/19 by Jianfa
# ------------------------------

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        
        left = intervals[-1][0]
        count = 0
        length = len(intervals)
        for pair in intervals[:length-1][::-1]:
            if pair[1] > left:
                count += 1
            else:
                left = pair[0]
        
        return count

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Similar idea from https://leetcode.com/problems/non-overlapping-intervals/discuss/91713/Java%3A-Least-is-Most
# Note that if order the intervals by the start value, traverse the list from the end
# The latest start interval, allow more possible non-overlap intervals in front of it
# In contrast, if order the intervals by the end value, traverse the list from the start