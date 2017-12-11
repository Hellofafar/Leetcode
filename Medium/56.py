# ------------------------------
# 56. Merge Intervals
# 
# Description:
# Given a collection of intervals, merge all overlapping intervals.
# 
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
# 
# Version: 1.0
# 12/10/17 by Jianfa
# ------------------------------

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x.start)
        res = []
        s = intervals[0].start
        e = intervals[0].end
        for item in intervals[1:]:
            if item.start <= e: 
                if item.end > e:
                    e = item.end
            else:
                temp = Interval(s, e)
                res.append(Interval(s, e))
                s = item.start
                e = item.end
        
        res.append(Interval(s, e))
                
        return res
        
# Used for testing
if __name__ == "__main__":
    test = Solution()
    intervals = [[1,4],[2,3]]

# ------------------------------
# Summary:
# For the merging condition, I used "if item.start <= e and item.end > e" as condition before, but it's 
# wrong because I eliminate the situation when item.end <= e, it should also be merged although no change 
# to the range.