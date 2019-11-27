# ------------------------------
# 252. Meeting Rooms
# 
# Description:
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] 
# (si < ei), determine if a person could attend all meetings.
# 
# Example 1:
# Input: [[0,30],[5,10],[15,20]]
# Output: false
# 
# Example 2:
# Input: [[7,10],[2,4]]
# Output: true
# 
# Version: 1.0
# 11/26/19 by Jianfa
# ------------------------------

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals or not intervals[0]:
            return True
        
        intervals.sort(key=lambda x:x[0]) # sort by starting time
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        
        return True

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 