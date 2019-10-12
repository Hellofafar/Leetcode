# ------------------------------
# 436. Find Right Interval
# 
# Description:
# Given a set of intervals, for each of the interval i, check if there exists an interval j 
# whose start point is bigger than or equal to the end point of the interval i, which can be 
# called that j is on the "right" of i.
# 
# For any interval i, you need to store the minimum interval j's index, which means that the 
# interval j has the minimum start point to build the "right" relationship for interval i. If 
# the interval j doesn't exist, store -1 for the interval i. Finally, you need output the 
# stored value of each interval as an array.
# 
# Note:
# 
# You may assume the interval's end point is always bigger than its start point.
# You may assume none of these intervals have the same start point.
# 
# Example 1:
# Input: [ [1,2] ]
# Output: [-1]
# Explanation: There is only one interval in the collection, so it outputs -1.
# 
# Example 2:
# Input: [ [3,4], [2,3], [1,2] ]
# Output: [-1, 0, 1]
# Explanation: There is no satisfied "right" interval for [3,4].
# For [2,3], the interval [3,4] has minimum-"right" start point;
# For [1,2], the interval [2,3] has minimum-"right" start point.
# 
# Example 3:
# Input: [ [1,4], [2,3], [3,4] ]
# Output: [-1, 2, -1]
# Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
# For [2,3], the interval [3,4] has minimum-"right" start point.
# 
# Version: 1.0
# 10/11/19 by Jianfa
# ------------------------------

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        l = sorted((e[0], i) for i, e in enumerate(intervals))
        
        res = []
        for e in intervals:
            r = bisect.bisect_left(l, (e[1],)) # This is to find the minimum start point to build the "right" relationship for interval e
            res.append(l[r][1] if r < len(intervals) else -1)
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Binary search idea from: https://leetcode.com/problems/find-right-interval/discuss/91806/Python-O(nlogn)-short-solution-with-explanation
# For each end point search for the first start point that is equal or higher in a 
# previously constructed ordered list of start points. If there is one then return 
# its index. If not return -1