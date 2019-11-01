# ------------------------------
# 32. Longest Valid Parentheses
# 
# Description:
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
# 
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
# 
# Version: 1.0
# 10/23/17 by Jianfa
# ------------------------------

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        max_len = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                stack.pop()
                if not stack:  # If stack is empty after popping out the top element
                    stack.append(i)
                else:
                    if i - stack[-1] > max_len:
                        max_len = i - stack[-1]
        
        return max_len
        
      
# Used for test
if __name__ == "__main__":
    test = Solution()
    s = ''
    
    print(test.longestValidParentheses(s))

# ------------------------------
# Summary:
# Implement stack solution.
# Let the stack start with -1. 
# When a "(" is met, push the index of "(" in the stack.
# When a ")" is met, pop the top item out. Then subtract the current top item from the index of ")". The result
# is length of current valid string of parentheses.
# If the stack becomes empty after popping, which means there are no matching "(" for this ")", push the index 
# of ")" in the stack.
# Replace the max_len if curr_len is greater.
# 
# O(n) time, O(n) space