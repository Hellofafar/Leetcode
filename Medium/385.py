# ------------------------------
# 385. Mini Parser
# 
# Description:
# Given a nested list of integers represented as a string, implement a parser to deserialize it.
# 
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
# 
# Note: You may assume that the string is well-formed:
# 
# String is non-empty.
# String does not contain white spaces.
# String contains only digits 0-9, [, - ,, ].
# 
# Example 1:
# Given s = "324",
# You should return a NestedInteger object which contains a single integer 324.
# 
# Example 2:
# Given s = "[123,[456,[789]]]",
# Return a NestedInteger object containing a nested list with 2 elements:
# 
# 1. An integer containing value 123.
# 2. A nested list containing two elements:
#     i.  An integer containing value 456.
#     ii. A nested list with one element:
#          a. An integer containing value 789.
# 
# Version: 1.0
# 09/30/19 by Jianfa
# ------------------------------

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return None
        if s[0] != "[":
            # Special case
            return NestedInteger(int(s))
        
        stack = []
        curr = None
        
        l = 0
        for r in range(len(s)):
            ch = s[r]
            if ch == "[":
                if curr is not None:
                    stack.append(curr)
                curr = NestedInteger()
                l = r + 1
            elif ch == "]":
                num = s[l:r]
                if len(num) > 0:
                    curr.add(NestedInteger(int(num)))
                if stack:
                    pop = stack.pop()
                    pop.add(curr)
                    curr = pop
                l = r + 1
            elif ch == ",":
                if s[r-1] != "]":
                    # If it's a number before comma
                    num = s[l:r]
                    curr.add(NestedInteger(int(num)))
                l = r + 1
        
        return curr

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow the idea from: https://leetcode.com/problems/mini-parser/discuss/86066/An-Java-Iterative-Solution
# If encounters '[', push current NestedInteger to stack and start a new one.
# If encounters ']', end current NestedInteger and pop a NestedInteger from stack to continue.
# If encounters ',', append a new number to curr NestedInteger, if this comma is not right after a brackets.
# Update index l and r, where l shall point to the start of a integer substring, while r shall points to the end+1 of substring.