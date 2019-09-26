# ------------------------------
# 307. Range Sum Query - Mutable
# 
# Description:
# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
# The update(i, val) function modifies nums by updating the element at index i to val.
# 
# Example:
# Given nums = [1, 3, 5]
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# 
# Note:
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is distributed evenly.
# 
# Version: 1.0
# 09/25/19 by Jianfa
# ------------------------------

class NumArray:

    def __init__(self, nums: List[int]):
        if len(nums) > 0:
            self.n = len(nums)
            self.tree = [0 for _ in range(self.n * 2)]
            self.buildTree(nums)
            
    def buildTree(self, nums: List[int]):
        i = self.n
        j = 0
        while i < 2 * self.n:
            self.tree[i] = nums[j]
            i += 1
            j += 1
        i = self.n - 1
        while i > 0:
            self.tree[i] = self.tree[i*2] + self.tree[i*2 + 1]
            i -= 1
        
    def update(self, i: int, val: int) -> None:
        index = i + self.n
        self.tree[index] = val
        while index > 0:
            left = index
            right = index
            if index % 2 == 0:
                right = index + 1
            else:
                left = index - 1 
            
            self.tree[index//2] = self.tree[left] + self.tree[right]
            index //= 2

    def sumRange(self, i: int, j: int) -> int:
        l = i + self.n
        r = j + self.n
        summ = 0
        while l <= r:
            if l % 2 == 1:
                summ += self.tree[l]
                l += 1
            if r % 2 == 0:
                summ += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        
        return summ

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Segment tree iterative solution.
# Segment Tree can be broken down to the three following steps:
# 
# 1. Pre-processing step which builds the segment tree from a given array.
# 2. Update the segment tree when an element is modified.
# 3. Calculate the Range Sum Query using the segment tree.
# See details: https://leetcode.com/articles/range-sum-query-mutable/
# Recursive solution: https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/
# Use binary indexed tree: https://leetcode.com/problems/range-sum-query-mutable/discuss/75753/Java-using-Binary-Indexed-Tree-with-clear-explanation
