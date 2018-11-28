# ------------------------------
# 253. Meeting Rooms II
# 
# Description:
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
# 
# Example 1:
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# 
# Example 2:
# Input: [[7,10],[2,4]]
# Output: 1
# 
# Version: 1.0
# 10/20/18 by Jianfa
# ------------------------------

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals.sort(key=lambda interval: interval.start)
        rooms = [intervals[0].end]
        heapq.heapify(rooms)  # rooms is a heap to record the latest ending time being used
        
        for itv in intervals[1:]:
            s = itv.start
            e = itv.end
            earliestEndTime = rooms[0]
            
            if s >= earliestEndTime:  # If there is a room ends no later than start time, the room can be used and update end time
                heapq.heapreplace(rooms, e)
                
                
            else:                     # If there is no available room, just add a new room with new end time
                heapq.heappush(rooms, e)

        return len(rooms)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Allocate the rooms according to start time
# For rooms, there are two states:
# 1. there is at least one room's end time is no later than start time of next interval
# 2. all rooms' end times are later than start time of next interval
# For 1, just keep using the room
# For 2, allocate a new room
# Use a heap to store the end time of every rooms, and compare the earliest end time with
# next start time to decide the allocation of room.