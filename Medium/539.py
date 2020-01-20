# ------------------------------
# 539. Minimum Time Difference
# 
# Description:
# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes 
# difference between any two time points in the list.
# 
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# 
# Note:
# The number of time points in the given list is at least 2 and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.
# 
# Version: 1.0
# 01/18/20 by Jianfa
# ------------------------------

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = [False] * 24 * 60
        for point in timePoints:
            hour = int(point.split(":")[0])
            minute = int(point.split(":")[1])
            if times[hour * 60 + minute]:
                # duplicate time point appears
                return 0
            times[hour * 60 + minute] = True
            
        small = 1440 # smallest time point in times list
        large = 0    # largest time point in times list
        prev = 0     # last time point
        diff = 1440
        for i in range(1440):
            if times[i]:
                if small != 1440:
                    # current i is not the first time point
                    diff = min(diff, i - prev)
                small = min(small, i)
                large = max(large, i)      # update largest time point
                prev = i
        
        print(small, large)
        diff = min(diff, 1440 - large + small)
        return diff
            

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from: https://leetcode.com/problems/minimum-time-difference/discuss/100640/Verbose-Java-Solution-Bucket