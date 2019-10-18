# ------------------------------
# 528. Random Pick with Weight
# 
# Description:
# Given an array w of positive integers, where w[i] describes the weight of index i, write a 
# function pickIndex which randomly picks an index in proportion to its weight.
# 
# Note:
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
# 
# Example 1:
# Input: 
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
# 
# Example 2:
# Input: 
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
# Explanation of Input Syntax:
# 
# The input is two lists: the subroutines called and their arguments. Solution's constructor has 
# one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, 
# even if there aren't any.
# 
# Version: 1.0
# 10/17/19 by Jianfa
# ------------------------------

from bisect import bisect_left

class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i-1]
        self.wList = w

    def pickIndex(self) -> int:
        n = random.randint(1, self.wList[-1])
        return bisect_left(self.wList, n)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Binary search idea from https://leetcode.com/problems/random-pick-with-weight/discuss/154044/Java-accumulated-freq-sum-and-binary-search
# Use accumulated frequency sum to form a selection range, so that enable representing 
# weight by the numbers in the range.
# 
# O(nlogn) time, O(n) space