# ------------------------------
# 681. Next Closest Time
# 
# Description:
# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. 
# There is no limit on how many times a digit can be reused.
# 
# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. 
# "1:34", "12:9" are all invalid.
# 
# Example 1:
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later. 
# It is not 19:33, because this occurs 23 hours and 59 minutes later.
# 
# Example 2:
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the 
# returned time is next day's time since it is smaller than the input time numerically.
# 
# Version: 1.0
# 10/25/17 by Jianfa
# ------------------------------

import itertools

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        h1 = int(time[0])
        h2 = int(time[1])
        m1 = int(time[3])
        m2 = int(time[4])
        nums = [h1, h2, m1, m2]
        
        groups = itertools.permutations(nums, 2)
        
        # Check if there exists minutes that in the range (m1m2, 59]
        candidates = [10 * x[0] + x[1] for x in groups]
        candidates.extend([10 * h1 + h1, 10 * h2 + h2, 10 * m1 + m1, 10 * m2 + m2])
        candidates = list(set(candidates))
        candidates.sort()
        mm = 10 * m1 + m2
        mm_idx = candidates.index(mm)
        
        if mm_idx + 1 < len(candidates) and candidates[mm_idx + 1] <= 59:
            new_mm = candidates[mm_idx + 1]
            if new_mm < 10:
                return "%d%d:%d%d" % (h1, h2, 0, new_mm)
            else:
                return "%d%d:%d" % (h1, h2, new_mm)
        
        # Check other hours
        hh = 10 * h1 + h2
        hh_idx = candidates.index(hh)
        
        # If exist hour in (h1h2, 23]
        if hh_idx + 1 < len(candidates) and candidates[hh_idx + 1] <= 23:
            new_hh = candidates[hh_idx + 1]
            new_mm = candidates[0]
            if new_hh < 10:
                new_hh = "0%d" % new_hh
            else:
                new_hh = str(new_hh)
            
            if new_mm < 10:
                new_mm = "0%d" % new_mm
            else:
                new_mm = str(new_mm)
                
            return new_hh + ":" + new_mm
        
        # If not exist hour in (h1h2, 23]
        else:
            new_hh = new_mm = candidates[0]
            if new_hh < 10:
                return "%d%d:%d%d" % (0, new_hh, 0, new_mm)
            else:
                return str(new_hh) + ":" + str(new_mm)

# Used for test
if __name__ == "__main__":
    test = Solution()
    time = "21:56"

    print(test.nextClosestTime(time))

# ------------------------------
# Summary:
# My idea is to check the hour at first, then check the minutes. Assume original time is h1h2:m1m2
# For the same hour, if there exists a minute combination mimj that in the range (m1m2, 59], then return h1h2:mimj
# If not, then check another hour.
# If there exists a hour combination hihj that in the range (h1h2, 23], then find the smallest combination mimj,
# return hihj:mimj.
# If no hour in (h1h2, 23], find the smallest combination ninj, return ninj:ninj. Actually ni/nj should be the same.
