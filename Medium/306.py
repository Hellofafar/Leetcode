# ------------------------------
# 306. Additive Number
# 
# Description:
# Additive number is a string whose digits can form additive sequence.
# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent 
# number in the sequence must be the sum of the preceding two.
# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
# 
# Example 1:
# Input: "112358"
# Output: true
# Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
#              1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 
# Example 2:
# Input: "199100199"
# Output: true
# Explanation: The additive sequence is: 1, 99, 100, 199. 
#              1 + 99 = 100, 99 + 100 = 199
# 
# Constraints:
# 
# num consists only of digits '0'-'9'.
# 1 <= num.length <= 35
# 
# Follow up:
# How would you handle overflow for very large input integers?
# 
# Version: 1.0
# 09/24/19 by Jianfa
# ------------------------------

import itertools

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i, j in itertools.combinations(range(1, n), 2):
            if i <= n / 2:
                a = num[:i]
                b = num[i:j]
                if a[0] == '0' and i > 1 or b[0] == '0' and j - i > 1:
                    # Some string has leading zero
                    continue
                
                while j < n:
                    c = str(int(a) + int(b))
                    if not num.startswith(c, j):
                        break
                    j += len(c)
                    a, b = b, c
                
                if j == n:
                    return True
            
        return False

# Used for testing
if __name__ == "__main__":
    test = Solution()
    num = "012358"
    num = "199100199"

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/additive-number/discuss/75578/Python-solution
# Iterative solution: try all possibilities for first two numbers and check if it fits
# The first number will be at most n/2 long (n is digit number), which help decrease the combination number.
# For follow up, if using Java, BigInteger is a good idea:
# https://leetcode.com/problems/additive-number/discuss/75567/Java-Recursive-and-Iterative-Solutions