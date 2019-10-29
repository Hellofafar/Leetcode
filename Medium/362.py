# ------------------------------
# 362. Design Hit Counter
# 
# Description:
# Design a hit counter which counts the number of hits received in the past 5 minutes.
# 
# Each function accepts a timestamp parameter (in seconds granularity) and you may assume 
# that calls are being made to the system in chronological order (ie, the timestamp is 
# monotonically increasing). You may assume that the earliest timestamp starts at 1.
# 
# It is possible that several hits arrive roughly at the same time.
# 
# Example:
# 
# HitCounter counter = new HitCounter();
# 
# // hit at timestamp 1.
# counter.hit(1);
# 
# // hit at timestamp 2.
# counter.hit(2);
# 
# // hit at timestamp 3.
# counter.hit(3);
# 
# // get hits at timestamp 4, should return 3.
# counter.getHits(4);
# 
# // hit at timestamp 300.
# counter.hit(300);
# 
# // get hits at timestamp 300, should return 4.
# counter.getHits(300);
# 
# // get hits at timestamp 301, should return 3.
# counter.getHits(301); 
# 
# Follow up:
# What if the number of hits per second could be very large? Does your design scale?
# 
# Version: 1.0
# 10/28/19 by Jianfa
# ------------------------------

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = [0] * 300
        self.hits = [0] * 300

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        time = timestamp % 300
        if self.times[time] != timestamp:
            # the first hit at this time
            self.times[time] = timestamp
            self.hits[time] = 1
        else:
            self.hits[time] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        total = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                total += self.hits[i]
        
        return total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Use two list to store timestamp and corresponding hits respectively. Since it's O(1) space
# don't worry about waste space with two lists.
# Idea from: https://leetcode.com/problems/design-hit-counter/discuss/83483/Super-easy-design-O(1)-hit()-O(s)-getHits()-no-fancy-data-structure-is-needed!
# 
# O(n) time (getHits), O(n) space