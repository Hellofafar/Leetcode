# ------------------------------
# 57. Insert Interval
# 
# Description:
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if 
# necessary).
# 
# You may assume that the intervals were initially sorted according to their start times.
# 
# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
# 
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
# 
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
# 
# Version: 1.0
# 12/19/17 by Jianfa
# ------------------------------

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        
        res = []
        startPos = len(intervals)  # Don't forget initialization
        endPos = len(intervals)
        for idx, itv in enumerate(intervals):
            if itv.start > newInterval.start:
                startPos = idx
                break
                
        for idx, itv in enumerate(intervals):
            if itv.start > newInterval.end:
                endPos = idx
                break
        
        if startPos == 0:
            if endPos == 0:
                res.append(newInterval)
                res.extend(intervals)
                return res
            
            else:
                prev = intervals[endPos-1]
                if prev.end <= newInterval.end:
                    res.append(newInterval)
                    res.extend(intervals[endPos:])
                else:
                    temp = Interval(newInterval.start, prev.end)
                    res.append(temp)
                    res.extend(intervals[endPos:])
                return res
        
        else:
            prev1 = intervals[startPos-1]
            prev2 = intervals[endPos-1]
            if prev1.end < newInterval.start:  # No merge with prev1
                if prev2.end < newInterval.end:
                    res.extend(intervals[:startPos])
                    res.append(newInterval)
                    res.extend(intervals[endPos:])
                
                else:
                    temp = Interval(newInterval.start, prev2.end)
                    res.extend(intervals[:startPos])
                    res.append(temp)
                    res.extend(intervals[endPos:])
                return res
            
            else:
                if prev2.end < newInterval.end:
                    temp = Interval(prev1.start, newInterval.end)
                    res.extend(intervals[:startPos-1])
                    res.append(temp)
                    res.extend(intervals[endPos:])
                
                else:
                    temp = Interval(prev1.start, prev2.end)
                    res.extend(intervals[:startPos-1])
                    res.append(temp)
                    res.extend(intervals[endPos:])
                return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Find start and end position for newInterval respectively
# Then compare the start value and end value to decide whether to merge