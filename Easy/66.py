# ------------------------------
# 66. Plus One
# 
# Description:
# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# The digits are stored such that the most significant digit is at the head of the list.
# 
# Version: 1.0
# 11/04/17 by Jianfa
# ------------------------------

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[0] == 0:
            return [1]
        
        for i in range(len(digits))[::-1]:
            temp = digits[i] + 1
            if temp / 10 > 0:
                digits[i] = temp % 10
            else:
                digits[i] = temp
                break
        
        if digits[0] == 0:
            digits.insert(0, 1)
            
        return digits


# Used for test
if __name__ == "__main__":
    test = Solution()
    digits = [0]

    print(test.plusOne(digits))


# ------------------------------
# Summary:
# Calculate from end to start.