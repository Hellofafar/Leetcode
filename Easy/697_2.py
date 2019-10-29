# ------------------------------
# 697. Degree of an Array
# 
# Description:
# 
# 
# Version: 2.0
# 10/28/19 by Jianfa
# ------------------------------

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        # Find the left index and right index and count of each number
        for i, n in enumerate(nums):
            if n not in left:
                left[n] = i
            right[n] = i
            count[n] = count.get(n, 0) + 1
        
        res = len(nums)
        degree = max(count.values())
        # check every number has the max degree
        for n in count:
            if count[n] == degree:
                res = min(res, right[n] - left[n] + 1)
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Left and right index from https://leetcode.com/problems/degree-of-an-array/solution/
# O(n) times, O(n) space