# ------------------------------
# 146. LRU Cache
# 
# Description:
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

# Version: 1.0
# 10/28/18 by Jianfa
# ------------------------------

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.order = []
        self.capacity = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            if key != self.order[-1]:
                self.order.remove(key)
                self.order.append(key)
            return self.cache[key]
        
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache[key] = value
            if key != self.order[-1]:
                self.order.remove(key)
                self.order.append(key)
        
        else:
            if self.capacity == 0:
                evictKey = self.order.pop(0)
                del self.cache[evictKey]
            
            else:
                self.capacity -= 1
            
            self.cache[key] = value
            self.order.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Stack + map solution.
# O(n) space complexity and O(n^2) time complexity