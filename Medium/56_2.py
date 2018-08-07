# ------------------------------
# 56. Merge Intervals
# 
# Description:
# 
# Version: 2.0
# 08/06/18 by Jianfa
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
        
        intervals.sort(key = lambda x: x.start)
        
        res = []
        cur = intervals[0]
        for i in intervals[1:]:
            if i.start <= cur.end:
                cur.end = max(cur.end, i.end)
            
            else:
                res.append(cur)
                cur = i
        
        res.append(cur)
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 