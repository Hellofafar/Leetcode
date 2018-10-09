# ------------------------------
# 128. Longest Consecutive Sequence
# 
# Description:
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# Your algorithm should run in O(n) complexity.
# 
# Example:
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# 
# Version: 1.0
# 10/08/18 by Jianfa
# ------------------------------

from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        sizeMap = defaultdict(int)
        
        for n in nums:
            if sizeMap[n] > 0:  # Duplicate
                continue
            
            if sizeMap[n-1] > 0 and sizeMap[n+1] > 0:  # If n can connect left and right subsequence
                leftSize = sizeMap[n-1]  # Get the size of longest consecutive sequence that has one end n-1
                rightSize = sizeMap[n+1] # Get the size of longest consecutive sequence that has one end n+1
                sizeMap[n-leftSize] = sizeMap[n+rightSize] = sizeMap[n] = leftSize + rightSize + 1  # Update two end's value to extend size
                
            elif sizeMap[n-1] > 0:                     # If only left side of n can add n into subsequence 
                leftSize = sizeMap[n-1]
                sizeMap[n-leftSize] = sizeMap[n] = leftSize + 1
                
            elif sizeMap[n+1] > 0:                     # If only right side of n can add n into subsequence 
                rightSize = sizeMap[n+1]
                sizeMap[n+rightSize] = sizeMap[n] = rightSize + 1
            
            else:                                      # If no subsequence can add n
                sizeMap[n] = 1
                
        print(sizeMap)
        
        return max(sizeMap.values())  # Return the max size value
            

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# The key idea is use the map to record largest size
# We can only update value for two ends of a subsequence.
# e.g. for (1,2,3,4), we can update map[1] = map[4] = 4, map[2] and map[3] can be 1.
# because only if we meet 5 or 0, then we need to extend the size of this subsequence,
# otherwise, size of this subsequence will keep same.