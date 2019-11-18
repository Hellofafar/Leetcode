# ------------------------------
# 57. Insert Interval
# 
# Description:
# Given a set of non-overlapping intervals, insert a new interval into the intervals 
# (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their start times.
# 
# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
# 
# Version: 2.0
# 11/17/19 by Jianfa
# ------------------------------

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not newInterval:
            return intervals
        elif not intervals:
            return [newInterval]
        
        left = 0 # index lf last intervals on the left unmerged
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                # stop to merge any other intervals
                return intervals[:left] + [newInterval] + intervals[i:]
            elif newInterval[0] <= intervals[i][1]:
                # find an overlapping intervals
                # update start and end bound of newInterval
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            else:
                left += 1
        
        # append newInterval to the end of intervals[:left]
        return intervals[:left] + [newInterval]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Key idea is to find where to start and where to end merging process.
# During process, update newInterval's start and end bound, insert newInterval to intervals
# until no more intervals can be merged.
# 
# O(N) time O(1) space