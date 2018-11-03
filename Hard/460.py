# ------------------------------
# 460. LFU Cache
# 
# Description:
# Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# LFUCache cache = new LFUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# Version: 1.0
# 11/02/18 by Jianfa
# ------------------------------

from collections import OrderedDict

class LFUCache: 

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.valueDict = {}  # value of key
        self.countDict = {}  # count of key
        self.frequencyDict = {}  # {fre, OrderedDict} keys of every frequency number. OrderedDict can be sorted so use it to record recently used order
        self.frequencyDict[1] = OrderedDict()
        self.min = -1  # least frequency so far
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.valueDict:
            return -1
        
        count = self.countDict[key]
        self.countDict[key] = count + 1
        del self.frequencyDict[count][key]  # remove key in previous frequencyDict[count]
        
        if count == self.min and len(self.frequencyDict[count]) == 0:  # If least frequency needs to add 1
            self.min += 1
        
        if count+1 not in self.frequencyDict:
            self.frequencyDict[count+1] = OrderedDict()
        
        self.frequencyDict[count+1][key] = 1  # {fre, {key:1}} add {key:1} to frequencyDict
        
        return self.valueDict[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity <= 0:
            return
        
        if key in self.valueDict:
            self.valueDict[key] = value
            self.get(key)  # Add frequency
            return
        
        if len(self.valueDict) >= self.capacity:  # It's over capacity
            leastFreq = self.frequencyDict[self.min].popitem(last=False)
            self.valueDict.pop(leastFreq[0])
            
        self.valueDict[key] = value  # key is not in valueDict, so add it
        self.countDict[key] = 1  # update countDict with {key:1}
        self.min = 1  # least frequency becomes to 1 again
        self.frequencyDict[self.min][key] = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow idea from https://leetcode.com/problems/lfu-cache/discuss/94521/JAVA-O(1)-very-easy-solution-using-3-HashMaps-and-LinkedHashSet
# Used a data structure from collections.OrderedDict