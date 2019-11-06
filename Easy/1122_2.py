# ------------------------------
# 1122. Relative Sort Array
# 
# Description:
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in 
# arr2 are also in arr1.
# 
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same 
# as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.
# 
# Example 1:
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
# 
# Constraints:
# 
# arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# Each arr2[i] is distinct.
# Each arr2[i] is in arr1.
# 
# Version: 1.0
# 11/05/19 by Jianfa
# ------------------------------

from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {a:i for i, a in enumerate(arr2)}                 # {a:index}
        return sorted(arr1, key=lambda a: order.get(a, a + 1000)) # sorted by a's index in order, if a not in order, than use a + 1000 instead

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Smart solution from: https://leetcode.com/problems/relative-sort-array/discuss/334585/Python-Straight-Forward-1-line-and-2-lines
# This make use of the constraint that arr1.length, arr2.length <= 1000, so for those
# elements of arr1 that don't appear in arr2, grant the index a + 1000 as its sorted 
# key in arr1.