# ------------------------------
# 167. Two Sum II - Input array is sorted
# 
# Description:
# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
# Note:
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.
# 
# Example:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
# 
# Version: 1.0
# 06/09/18 by Jianfa
# ------------------------------

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        unique = sorted(set(numbers))  # Set is not sorted
        for n in unique:
            if target - n in numbers:
                if n == target - n and numbers.count(n) > 1:
                    return [numbers.index(n) + 1, numbers.index(n) + 2]
                
                elif n == target - n and numbers.count(n) == 1:
                    continue
                
                else:
                    return [numbers.index(n) + 1, numbers.index(target - n) + 1]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 