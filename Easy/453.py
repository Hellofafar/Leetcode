# ------------------------------
# 453. Minimum Moves to Equal Array Elements
# 
# Description:
# Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
# Example:
# Input:
# [1,2,3]
# Output:
# 3
# Explanation:
# Only three moves are needed (remember each move increments two elements):
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
# 
# Version: 1.0
# 07/06/18 by Jianfa
# ------------------------------

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# This is a math problem.
# Assume after m moves, all the numbers become x, and n is the length of array.
# Then sum + m * (n - 1) = x * n
# minNum will always be the minimum until getting to be x, so x = minNum + m
# sum + m * (n - 1) = (minNum + m) * n
# m = sum - minNum * n
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/discuss/93817/It-is-a-math-question