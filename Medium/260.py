# ------------------------------
# 260. Single Number III
# 
# Description:
# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
# Example:
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# 
# Note:
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
# 
# Version: 1.0
# 09/27/18 by Jianfa
# ------------------------------

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        for i in nums:
            diff ^= i
            
        # To get the number with first digit that two target elements differ
        # e.g. 3 = 011 5 = 101, the first different digit for 3 and 5 is the first digit (rightmost one)
        diff &= -diff
        
        res = [0, 0]
        for i in nums:
            if i & diff:  # If i has '1' at the same digit as diff
                res[0] ^= i
                
            else:
                res[1] ^= i
                
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from https://leetcode.com/problems/single-number-iii/discuss/68900/Accepted-C++Java-O(n)-time-O(1)-space-Easy-Solution-with-Detail-Explanations
# See explanation: https://leetcode.com/problems/single-number-iii/discuss/68901/Sharing-explanation-of-the-solution