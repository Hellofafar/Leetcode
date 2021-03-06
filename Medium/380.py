# ------------------------------
# 380. Insert Delete GetRandom O(1)
# 
# Description:
# Design a data structure that supports all following operations in average O(1) time.
# 
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
# 
# Example:
# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();
# 
# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);
# 
# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);
# 
# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);
# 
# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();
# 
# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);
# 
# // 2 was already in the set, so return false.
# randomSet.insert(2);
# 
# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();
# 
# Version: 1.0
# 09/30/19 by Jianfa
# ------------------------------

import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = {}    

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pos:
            return False
        
        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pos:
            return False
        
        if self.pos[val] < len(self.nums) - 1:
            # if value is not in the last, swap the last one with this val
            idx, lastNum = self.pos[val], self.nums[-1]
            self.pos[lastNum], self.nums[idx] = idx, lastNum
        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0, len(self.nums)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from: https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85397/Simple-solution-in-Python
# Use list to store number which will be used when calling getRandom()
# Use dict to store val's index, enabling O(1) insertion and deletion