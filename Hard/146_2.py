# ------------------------------
# 146. LRU Cache
# 
# Description:
# 
# Version: 2.0
# 10/28/18 by Jianfa
# ------------------------------

class Node:
    def __init__(self, key, value):
        self.k = key
        self.v = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            n = self.cache[key]
            self._remove(n)
            self._add(n)
            
            return n.v
        
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            n = self.cache[key]
            self._remove(n)
            newNode = Node(key, value)
            self._add(newNode)
            self.cache[key] = newNode
            
        else:
            if self.capacity == 0:
                first = self.head.next
                self._remove(first)
                del self.cache[first.k]      
            
            else:
                self.capacity -= 1
            
            newNode = Node(key, value)
            self._add(newNode)
            self.cache[key] = newNode
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = p

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Double links + map solution from https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-+-Double-LinkedList
# The key idea is to create a class with double links, and design own remove() and add()
# function as python built-in function for list.