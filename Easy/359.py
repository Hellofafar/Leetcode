# ------------------------------
# 359. Logger Rate Limiter
# 
# Description:
# Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.
# 
# Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.
# 
# It is possible that several messages arrive roughly at the same time.
# 
# Example:
# Logger logger = new Logger();
# 
# // logging string "foo" at timestamp 1
# logger.shouldPrintMessage(1, "foo"); returns true; 
# 
# // logging string "bar" at timestamp 2
# logger.shouldPrintMessage(2,"bar"); returns true;
# 
# // logging string "foo" at timestamp 3
# logger.shouldPrintMessage(3,"foo"); returns false;
# 
# // logging string "bar" at timestamp 8
# logger.shouldPrintMessage(8,"bar"); returns false;
# 
# // logging string "foo" at timestamp 10
# logger.shouldPrintMessage(10,"foo"); returns false;
# 
# // logging string "foo" at timestamp 11
# logger.shouldPrintMessage(11,"foo"); returns true;
# 
# Version: 1.0
# 11/27/18 by Jianfa
# ------------------------------

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeDict = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.timeDict:
            self.timeDict[message] = timestamp
            return True
        
        else:
            if timestamp - self.timeDict[message] >= 10:
                self.timeDict[message] = timestamp
                return True
            
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Use map to record last print out timestamp.
# 
# A very smart idea: https://leetcode.com/problems/logger-rate-limiter/discuss/83273/Short-C++JavaPython-bit-different
# Instead of logging print times, I store when it's ok for a message to be printed again.
# 
# class Logger(object):
#     def __init__(self):
#         self.ok = {}
# 
#     def shouldPrintMessage(self, timestamp, message):
#         if timestamp < self.ok.get(message, 0):
#             return False
#         self.ok[message] = timestamp + 10
#         return True