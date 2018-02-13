# ------------------------------
# 757. Set Intersection Size At Least Two
# 
# Description:
# An integer interval [a, b] (for integers a < b) is a set of all consecutive integers from a to 
# b, including a and b.
# 
# Find the minimum size of a set S such that for every integer interval A in intervals, the 
# intersection of S with A has size at least 2.
# 
# Example 1:
# Input: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
# Output: 3
# Explanation:
# Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
# Also, there isn't a smaller size set that fulfills the above condition.
# Thus, we output the size of this set, which is 3.
# 
# Example 2:
# Input: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
# Output: 5
# Explanation:
# An example of a minimum sized set is {1, 2, 3, 4, 5}.
# 
# Version: 1.0
# 01/22/18 by Jianfa
# ------------------------------

class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda (s, e): (s, -e))

        cover = [2 for x in range(len(intervals))]

        res = 0
        while intervals:
            last = intervals.pop()
            step = cover.pop()

            for n in range(last[0], last[0] + step):
                for idx, pair in enumerate(intervals):
                    if cover[idx] and n <= pair[1]:
                        cover[idx] -= 1

                res += 1

        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow the idea in Solution section.
# The most awesome part is in the cover list. It can be used to record how many numbers in an
# interval need to be added to set S, in order to make S meets the conditions.