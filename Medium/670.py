# ------------------------------
# 670. Maximum Swap
# 
# Description:
# Given a non-negative integer, you could swap two digits at most once to get the 
# maximum valued number. Return the maximum valued number you could get.
# 
# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# 
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
# 
# Note:
# The given number is in the range [0, 108]
# 
# Version: 1.0
# 10/29/19 by Jianfa
# ------------------------------

class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num
        
        digitList = list(str(num))
        i = 1
        while i < len(digitList) and digitList[i] <= digitList[i-1]:
            # find the first index i to make digitList[i] > digitList[i-1]
            i += 1
        
        if i == len(digitList):
            # the digits are sorted in descending
            return num
        
        maxDigit = digitList[i]
        maxIndex = i
        for j in range(i+1, len(digitList)):
            # find the max digit in digitList[i:]
            # NOTE: it should be digitList[j] >= maxDigit because we want to use the latter one to swap so we can make sure number after swapping is largest
            # e.g. 1993 -> 9913
            if digitList[j] >= maxDigit:
                maxDigit = digitList[j]
                maxIndex = j
                
        for j in range(i):
            # find the first digit in digitList[:i] that is smaller than maxDigit
            if maxDigit > digitList[j]:
                digitList[j], digitList[maxIndex] = maxDigit, digitList[j]
                break
        
        return int("".join(digitList))

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Find the first digit that is larger than its previous digit, let say num[i]
# Then find the largest digit in the rest digits
# Swap the largest digit with the first digit that is smaller than it in the num[:i]
# This is not a concise solution