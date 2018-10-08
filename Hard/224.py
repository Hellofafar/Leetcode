# ------------------------------
# 224. Basic Calculator
# 
# Description:
# Implement a basic calculator to evaluate a simple expression string.
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
# Example 1:
# Input: "1 + 1"
# Output: 2
# 
# Example 2:
# Input: " 2-1 + 2 "
# Output: 3
# 
# Example 3:
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# 
# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
# 
# Version: 1.0
# 10/07/18 by Jianfa
# ------------------------------

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0  # temp result
        number = 0  # get every number in the string
        sign = 1  # indicate the operator
        
        for x in s:
            if x.isdigit():
                number = 10 * number + int(x)
            
            elif x == "+":
                res += sign * number
                number = 0
                sign = 1
                
            elif x == "-":
                res += sign * number
                number = 0
                sign = -1
                
            elif x == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            
            elif x == ")":
                res += sign * number
                number = 0
                res *= stack.pop()  # Get sign before opening parentheses, if "+" means positive, else negative
                res += stack.pop()  # Get result before opening parentheses, simply add it
        
        print(res)
        res += sign * number  # There may be a last number not counted
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Iterative solution.
# Use res to store temporal result, number to store every number, sign to denote positive
# or negative of the number.
# Once a "+" or "-" is met, add the number to res
# Once a "(" or ")" is met, push the res and sign or pop the res and sign