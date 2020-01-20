# ------------------------------
# 537. Complex Number Multiplication
# 
# Description:
# Given two strings representing two complex numbers.
# 
# You need to return a string representing their multiplication. Note i2 = -1 according to 
# the definition.
# 
# Example 1:
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form 
# of 0+2i.
# 
# Example 2:
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form 
# of 0+-2i.
# 
# Note:
# The input strings will not have extra blank.
# The input strings will be given in the form of a+bi, where the integer a and b will both 
# belong to the range of [-100, 100]. And the output should be also in this form.
# 
# Version: 1.0
# 01/17/20 by Jianfa
# ------------------------------

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        n1 = a.split("+")
        x1 = int(n1[0])
        y1 = int(n1[1].split("i")[0])
        
        n2 = b.split("+")
        x2 = int(n2[0])
        y2 = int(n2[1].split("i")[0])
        
        x = x1 * x2 - y1 * y2
        y = x1 * y2 + x2 * y1
        return "{}+{}i".format(str(x), str(y))

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# (x1 + y1i) * (x2 + y2i) = x1x2 + y1y2 * i^2 + (x1y2 + x2y1)i