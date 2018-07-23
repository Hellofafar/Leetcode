# ------------------------------
# 594. Longest Harmonious Subsequence
# 
# Description:
# We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
# Example 1:
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# 
# Note: The length of the input array will not exceed 20,000.
# 
# Version: 1.0
# 07/22/18 by Jianfa
# ------------------------------

from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        maxlen = 0
        for key in counter:
            if key+1 in counter:
                maxlen = max(maxlen, counter[key] + counter[key+1])
        
        return maxlen

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Use hash map to count the times a number appear. Then traverse the map, for every key, if key + 1 also in
# the map, then add their times and compare with current max length.