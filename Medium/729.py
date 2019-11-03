# ------------------------------
# 729. My Calendar I
# 
# Description:
# Implement a MyCalendar class to store your events. A new event can be added if adding 
# the event will not cause a double booking.
# 
# Your class will have the method, book(int start, int end). Formally, this represents a 
# booking on the half open interval [start, end), the range of real numbers x such that 
# start <= x < end.
# 
# A double booking happens when two events have some non-empty intersection (ie., there 
# is some time that is common to both events.)
# 
# For each call to the method MyCalendar.book, return true if the event can be added to 
# the calendar successfully without causing a double booking. Otherwise, return false and 
# do not add the event to the calendar.
# 
# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
# 
# Example 1:
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(15, 25); // returns false
# MyCalendar.book(20, 30); // returns true
# Explanation: 
# The first event can be booked.  The second can't because time 15 is already booked by another event.
# The third event can be booked, as the first event takes every time less than 20, but not including 20.
# 
# Note:
# 
# The number of calls to MyCalendar.book per test case will be at most 1000.
# In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
# 
# Version: 1.0
# 11/02/19 by Jianfa
# ------------------------------

import bisect

class MyCalendar:

    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        if not self.starts:
            self.starts.append(start)
            self.ends.append(end)
            return True
        else:
            index = bisect.bisect(self.starts, start)
            if index == 0:
                # if start value is smaller than all previous starts
                if end > self.starts[0]:
                    # there is overlap with the first range
                    return False
                else:
                    self.starts.insert(0, start)
                    self.ends.insert(0, end)
                    return True
            elif index == len(self.starts):
                # if start value is greater than all previous starts
                if start < self.ends[-1]:
                    # there is overlap with the last range
                    return False
                else:
                    self.starts.append(start)
                    self.ends.append(end)
                    return True
            else:
                if start < self.ends[index-1] or end > self.starts[index]:
                    return False
                else:
                    self.starts.insert(index, start)
                    self.ends.insert(index, end)
                    return True
                

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Binary search solution.
# Store the start and end of each range. When a new book check is coming, binary search
# the index for new range. If it's valid, update the start and end list, otherwise return
# false.
# 
# O(n^2) time for insert, O(n) space