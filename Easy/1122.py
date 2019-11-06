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
        arr2set = set(arr2)
        res = []    # final sorted result
        others = [] # elements that don't appear in arr2
        
        for n in arr1:
            if n not in arr2set:
                others.append(n)
        others.sort()
        
        counter = Counter(arr1) # count the number of each target element in arr1 
        for n in arr2:
            for _ in range(counter[n]):
                res.append(n)
        
        res.extend(others) # res plus the other elements not appeared in arr2
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Intuition: find the arr1's elements not shown in arr2 first and sort them.
# For the elements sorted in relative way, count each element and then append the number
# of elements to result list one by one based on arr2 order.
# 
# O(K * logK) + O(n - K) time, K is number of arr1's elements not shown in arr2
# O(n) space