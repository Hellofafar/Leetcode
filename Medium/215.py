# ------------------------------
# 215. Kth Largest Element in an Array
# 
# Description:
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Example 1:
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# Example 2:
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Version: 1.0
# 09/04/18 by Jianfa
# ------------------------------

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k-1]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 