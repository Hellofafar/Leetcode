# ------------------------------
# 4. Median of Two Sorted Arrays
# 
# Description:
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# Version: 1.0
# 11/12/19 by Jianfa
# ------------------------------

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        l = self.getKth(nums1, m, nums2, n, (m + n + 1) // 2)
        
        if (m + n) % 2 == 1:
            # if m + n is odd, then return the median number directly
            return l
        
        # m + n is even, need to get the right median one
        # then true median = (l + r) / 2
        r = self.getKth(nums1, m, nums2, n, (m + n + 2) // 2)
        return (l + r) / 2
    
    def getKth(self, nums1, m, nums2, n, k):
        # m is len of nums, n is len of nums2, find the kth number
        if m > n: # let m <= n
            return self.getKth(nums2, n, nums1, m, k)
        if m == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        
        i = min(m, k // 2)
        j = min(n, k // 2)
        if nums1[i-1] < nums2[j-1]:
            # eliminate the first i elements of nums1
            return self.getKth(nums1[i:], m - i, nums2, n, k - i)
        else:
            return self.getKth(nums1, m, nums2[j:], n - j, k - j)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2499/Share-my-simple-O(log(m+n))-solution-for-your-reference
# 
# O(log(M + N)) time