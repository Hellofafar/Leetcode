# ------------------------------
# 414. Third Maximum Number
# 
# Description:
# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
# Example 1:
# Input: [3, 2, 1]
# Output: 1
# Explanation: The third maximum is 1.
# 
# Example 2:
# Input: [1, 2]
# Output: 2
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# 
# Example 3:
# Input: [2, 2, 3, 1]
# Output: 1
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.
# 
# Version: 1.0
# 07/02/18 by Jianfa
# ------------------------------

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        time = 3
        maximum = nums[-1]
        last = nums[-1] + 1
        while nums and time:
            cur = nums.pop()
            if cur != last:
                time -= 1
                last = cur
        
        if time > 0:
            return maximum
        
        else:
            return cur

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 