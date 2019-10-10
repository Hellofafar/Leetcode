# ------------------------------
# 402. Remove K Digits
# 
# Description:
# Given a non-negative integer num represented as a string, remove k digits from the 
# number so that the new number is the smallest possible.
# 
# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# 
# Example 1:
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# 
# Example 2:
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# 
# Example 3:
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.
# 
# Version: 1.0
# 10/09/19 by Jianfa
# ------------------------------

import heapq

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        
        digits = []
        for n in num:
            # whenever meet a digit which is less than the previous digit, discard the previous one
            while k > 0 and len(digits) > 0 and digits[-1] > n:
                digits.pop()
                k -= 1
            digits.append(n)
        
        # corner case like "1111"
        while k > 0:
            digits.pop()
            k -= 1
        
        # Remove the leading zeros
        head = 0
        while head < len(digits) - 1: # There should be at least one digit in the final result
            if digits[head] == '0':
                head += 1
            else:
                break

        return "".join(digits[head:])

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Stack and greedy idea from https://leetcode.com/problems/remove-k-digits/discuss/88708/Straightforward-Java-Solution-Using-Stack