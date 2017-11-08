# ------------------------------
# 346. Moving Average from Data Stream
# 
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
# 
# For example,
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
# 
# Version: 1.0
# 11/07/17 by Jianfa
# ------------------------------

class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.window = []
        # self.first = 0
        self.windowSum = 0
        self.windowSize = 0
        self.maxSize = size
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.windowSize < self.maxSize:
            self.window.append(val)
            self.windowSize += 1
            self.windowSum += val
            return self.windowSum / self.windowSize
        
        else:
            self.window.append(val)
            self.windowSum += val - self.window[0]
            self.window.remove(self.window[0])
            return self.windowSum / self.windowSize 


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)