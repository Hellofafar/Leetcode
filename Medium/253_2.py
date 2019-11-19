# ------------------------------
# 253. Meeting Rooms II
# 
# Description:
# Given an array of meeting time intervals consisting of start and end times 
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
# 
# Example 1:
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# 
# Example 2:
# Input: [[7,10],[2,4]]
# Output: 1
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to default code 
# definition to get new method signature.
# 
# Version: 2.0
# 11/18/19 by Jianfa
# ------------------------------

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        
        rooms = [] # store the end time of each room
        for itv in intervals:
            if not rooms or rooms[0] > itv[0]:
                heapq.heappush(rooms, itv[1])
            else:
                heapq.heapreplace(rooms, itv[1])
        
        return len(rooms)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# More consise implementation.