# ------------------------------
# 20. Valid Parentheses
# 
# Description:
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
# 
# Version: 1.0
# 09/17/17 by Jianfa
# ------------------------------

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_len = len(s)
        match = {'(':')', '[':']', '{':'}'}
        
        if str_len % 2 != 0:
            return False
        
        else:
            seq = []
            for char in s:
                if char in match:
                    seq.append(char)
                elif len(seq) > 0 and char == match[seq[-1]]:
                    seq.pop()
                else:
                    return False

            if len(seq) > 0:
                return False

            else:
                return True


# Used for test
# if __name__ == "__main__":
#     test = Solution()
#     strings = "[([]])"
    
#     print(test.isValid(strings))


# ------------------------------
# Summary:
# list.pop(): Remove the item at the given position in the list, and return it.
#             If no index is specified, a.pop() removes and returns the last item in the list.
# list.remove(): Remove the first item from the list whose value is x.
# 
# One of the mistake I made was using remove() rather than pop(). When the string was "[([" and 
# I wanted to remove(s[-1]), I actually removed the first '['.
# 
# Also can use: del s[-1]
# del: remove an item from a list given its index instead of its value. (No return as pop())