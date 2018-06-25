# ------------------------------
# 349. Intersection of Two Arrays
# 
# Description:
# Given two arrays, write a function to compute their intersection.
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
# Note:
# Each element in the result must be unique.
# The result can be in any order.
# 
# Version: 1.0
# 06/24/18 by Jianfa
# ------------------------------

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Set operation.