# ------------------------------
# 284. Peeking Iterator
# 
# Description:
# 
# Version: 1.0
# 09/30/18 by Jianfa
# ------------------------------

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = []
        while iterator.hasNext():
            self.iterator.append(iterator.next())

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.hasNext():
            return self.iterator[0]
        
        else:
            return None

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return self.iterator.pop(0)
        
        else:
            return None
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if len(self.iterator) > 0 else False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Use a list to represent iterator. May cost much space.
# Think about using provided method.