# ------------------------------
# 706. Design HashMap
# 
# Description:
# Design a HashMap without using any built-in hash table libraries.
# 
# To be specific, your design should include these functions:
# 
# put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists 
# in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if this map contains 
# no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.
# 
# Example:
# 
# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);          
# hashMap.put(2, 2);         
# hashMap.get(1);            // returns 1
# hashMap.get(3);            // returns -1 (not found)
# hashMap.put(2, 1);          // update the existing value
# hashMap.get(2);            // returns 1 
# hashMap.remove(2);          // remove the mapping for 2
# hashMap.get(2);            // returns -1 (not found) 
# 
# Note:
# 
# All keys and values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashMap library.
# 
# Version: 1.0
# 10/28/19 by Jianfa
# ------------------------------

class ListNode:
    def __init__(self, k, v):
        self.pair = (k, v)
        self.next = None
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.hashmap = [None] * self.m

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        n = key % self.m
        if self.hashmap[n] == None:
            self.hashmap[n] = ListNode(key, value)
        else:
            cur = self.hashmap[n]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value)
                    return
                if cur.next == None:
                    # cur is the last node in hashmap[n]
                    break
                cur = cur.next
            cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        n = key % self.m
        if self.hashmap[n] != None:
            cur = self.hashmap[n]
            while cur != None:
                if cur.pair[0] == key:
                    return cur.pair[1]
                cur = cur.next
            
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        n = key % self.m
        if self.hashmap[n] != None:
            cur = self.hashmap[n]
            if cur.pair[0] == key:
                self.hashmap[n] = cur.next
            else:
                while cur.next != None and cur.next.pair[0] != key:
                    cur = cur.next
                if cur.next != None:
                    cur.next = cur.next.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# ListNode solution from https://leetcode.com/problems/design-hashmap/discuss/185347/Hash-with-Chaining-Python
# At first I solved with an array with size 1000001, but that may waste too much spaces
# ListNode solution is more close to realistic solution, that is use limit list space but
# link the node which has the same hash code