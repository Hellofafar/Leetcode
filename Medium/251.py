# ------------------------------
# 251. Flatten 2D Vector
# 
# Description:
# Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.
# 
# Example:
# 
# Vector2D iterator = new Vector2D([[1,2],[3],[4]]);
# 
# iterator.next(); // return 1
# iterator.next(); // return 2
# iterator.next(); // return 3
# iterator.hasNext(); // return true
# iterator.hasNext(); // return true
# iterator.next(); // return 4
# iterator.hasNext(); // return false
# 
# Notes:
# 
# Please remember to RESET your class variables declared in Vector2D, as static/class 
# variables are persisted across multiple test cases. Please see here for more details.
# You may assume that next() call will always be valid, that is, there will be at least 
# a next element in the 2d vector when next() is called.
# 
# Follow up:
# As an added challenge, try to code it using only iterators in C++ or iterators in Java.
# 
# Version: 1.0
# 11/26/19 by Jianfa
# ------------------------------

class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.length = len(v)
        self.v = v
        self.outerIndex = 0
        self.innerIndex = 0

    def next(self) -> int:
        res = self.v[self.outerIndex][self.innerIndex]
        if self.innerIndex == len(self.v[self.outerIndex]) - 1:
            # if this element is the last one in the current sub-vector
            self.innerIndex = 0
            self.outerIndex += 1
        else:
            self.innerIndex += 1
        
        return res

    def hasNext(self) -> bool:
        while self.outerIndex < self.length and self.innerIndex == len(self.v[self.outerIndex]):
            self.outerIndex += 1
        
        return self.outerIndex < self.length


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# There were some edge cases I didn't think of.
# e.g. [[]] or [[], [3]]
# Empty sub-vector is possible, so in function hasNext() need to consider this situation.