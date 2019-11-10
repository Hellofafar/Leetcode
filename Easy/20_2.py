# ------------------------------
# 20. Valid Parentheses
# 
# Description:
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# 
# Example 1:
# Input: "()"
# Output: true
# 
# Example 2:
# Input: "()[]{}"
# Output: true
# 
# Example 3:
# Input: "(]"
# Output: false
# 
# Example 4:
# Input: "([)]"
# Output: false
# 
# Example 5:
# Input: "{[]}"
# Output: true
# 
# Version: 2.0
# 11/09/19 by Jianfa
# ------------------------------

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c == "(" or c == "[" or c == "{":
                # push left parentheses to stack
                stack.append(c)
            else:
                if not stack or mapping[c] != stack[-1]:
                    # if there is no parentheses in stack or parenthesis is not matched, return false
                    return False
                stack.pop()
        
        # Check if all parentheses have been matched
        return not stack
            

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Stack solution, store left parentheses.
# 
# O(n) time O(n) space.