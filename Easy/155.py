# ------------------------------
# 155. Min Stack
# 
# Description:
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# 
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
# 
# Version: 1.0
# 10/20/19 by Jianfa
# ------------------------------

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = sys.maxsize

    def push(self, x: int) -> None:
        if x <= self.minimum:
            # push the previous minimum to the stack if push operation will change the minimum
            # so it help record previous minimum if this element is popped out
            self.stack.append(self.minimum)
            self.minimum = x
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack:
            if self.stack.pop() == self.minimum:
                # if the popped out element is the current minimum
                # pop the stack again to get new minimum of rest stack
                self.minimum = self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# The trick point is how to define push and pop operation, since they may affect the result
# of minimum number in the stack.