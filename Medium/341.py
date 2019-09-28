# ------------------------------
# 341. Flatten Nested List Iterator
# 
# Description:
# Given a nested list of integers, implement an iterator to flatten it.
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
# 
# Example 1:
# Input: [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false, 
#              the order of elements returned by next should be: [1,1,2,1,1].
# 
# Example 2:
# Input: [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false, 
#              the order of elements returned by next should be: [1,4,6].
# 
# Version: 1.0
# 09/27/19 by Jianfa
# ------------------------------

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flatList = []
        self.index = 0
        def flattenList(nestedList):
            for i in nestedList:
                if i.isInteger():
                    self.flatList.append(i.getInteger())
                else:
                    childList = i.getList()
                    flattenList(childList)
        flattenList(nestedList)

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.flatList[self.index - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.flatList)
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# flattenList func in the init function should be noted. There may be multi-level nested list.