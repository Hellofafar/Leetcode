# ------------------------------
# 258. Add Digits
# 
# Description:
# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
# Example:
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
# 
# Version: 1.0
# 06/23/18 by Jianfa
# ------------------------------

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            temp = 0
            while num:
                temp += num % 10
                num = num / 10
            num = temp
        return num

        ## Math solution
        if num == 0:
            return 0

        return 1 + (num - 1) % 9

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 1st solution: use while loop
# 2st solution: math solution. https://leetcode.com/problems/add-digits/discuss/68580/Accepted-C++-O(1)-time-O(1)-space-1-Line-Solution-with-Detail-Explanations