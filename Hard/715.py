# ------------------------------
# 715. Range Module
# 
# Description:
# A Range Module is a module that tracks ranges of numbers. Your task is to design and 
# implement the following interfaces in an efficient manner.

# addRange(int left, int right) Adds the half-open interval [left, right), tracking every 
# real number in that interval. Adding an interval that partially overlaps with currently 
# tracked numbers should add any numbers in the interval [left, right) that are not already 
# tracked.
# 
# queryRange(int left, int right) Returns true if and only if every real number in the 
# interval [left, right) is currently being tracked.
# 
# removeRange(int left, int right) Stops tracking every real number currently being tracked 
# in the interval [left, right).
# 
# Example 1:
# addRange(10, 20): null
# removeRange(14, 16): null
# queryRange(10, 14): true (Every number in [10, 14) is being tracked)
# queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
# queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
# 
# Note:
# 
# A half open interval [left, right) denotes all real numbers left <= x < right.
# 0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
# The total number of calls to addRange in a single test case is at most 1000.
# The total number of calls to queryRange in a single test case is at most 5000.
# The total number of calls to removeRange in a single test case is at most 1000.
# 
# Version: 1.0
# 11/20/19 by Jianfa
# ------------------------------

from bisect import bisect_left as bl, bisect_right as br
class RangeModule:

    def __init__(self):
        self.range = [] # 【left, right, left, right, ...]

    def addRange(self, left: int, right: int) -> None:
        li = bl(self.range, left)
        ri = br(self.range, right)
        self.range[li:ri] = [left] * (li % 2 == 0) + [right] * (ri % 2 == 0)

    def queryRange(self, left: int, right: int) -> bool:
        # NOTE: for left index, use bisect_left, for right index, use bisect_right
        li = br(self.range, left)
        ri = bl(self.range, right)
        return li == ri and li % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        li = bl(self.range, left)
        ri = br(self.range, right)
        self.range[li:ri] = [left] * (li % 2 == 1) + [right] * (ri % 2 == 1)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Impressive solution from https://leetcode.com/problems/range-module/discuss/169353/Ultra-concise-Python-(only-6-lines-of-actual-code)-(also-236ms-beats-100)
# 
# Use a list to store left and right bounds