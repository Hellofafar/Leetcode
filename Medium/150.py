# ------------------------------
# 150. Evaluate Reverse Polish Notation
# 
# Description:
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
# 
# Note:
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
# 
# Example 1:
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# Example 2:
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# 
# Example 3:
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# Version: 1.0
# 08/25/18 by Jianfa
# ------------------------------

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for x in tokens:
            if x not in ('+', '-', '*', '/'):
                stack.append(int(x))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if x == '+':
                    stack.append(n1 + n2)
                elif x == '-':
                    stack.append(n1 - n2)
                elif x == '*':
                    stack.append(n1 * n2)
                else:
                    temp = n1 / n2
                    if temp < 0 and n1 % n2 != 0:
                        temp += 1
                    stack.append(temp)
            
        return stack[0]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Note "Division between two integers should truncate toward zero.", so 6 / -132 = 0 rather than -1