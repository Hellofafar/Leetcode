# ------------------------------
# 227. Basic Calculator II
# 
# Description:
# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
# Example 1:
# Input: "3+2*2"
# Output: 7
# 
# Example 2:
# Input: " 3/2 "
# Output: 1
# 
# Example 3:
# Input: " 3+5 / 2 "
# Output: 5
# 
# Version: 1.0
# 09/20/18 by Jianfa
# ------------------------------

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return
        
        stack = []
        num = 0
        sign = '+'
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = 10*num + int(s[i])
            
            if not s[i].isdigit() and s[i] != ' ' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    lastNum = stack.pop()
                    if lastNum < 0 and lastNum % num != 0:
                        stack.append(lastNum / num + 1)  # if lastNum is negative, then division result is a little strange
                    else:
                        stack.append(lastNum / num)
                
                sign = s[i]
                num = 0
        
        return sum(stack)
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow idea from https://leetcode.com/problems/basic-calculator-ii/discuss/63003/Share-my-java-solution