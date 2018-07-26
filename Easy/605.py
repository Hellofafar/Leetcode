# ------------------------------
# 605. Can Place Flowers
# 
# Description:
# Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# 
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# 
# Note:
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.
# 
# Version: 1.0
# 07/22/18 by Jianfa
# ------------------------------

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if 1 not in flowerbed:
            if len(flowerbed) % 2 == 0:
                return len(flowerbed) / 2 >= n
            
            else:
                return len(flowerbed) / 2 + 1 >= n
        
        total = 0
        hasLeft = False
        hasRight = False
        count = 0
        for i in flowerbed:
            if i == 0:
                count += 1
            
            else:
                hasRight = True
                if hasLeft:
                    total += (count - 1) / 2
                else:
                    total += count / 2
                count = 0
                hasLeft = True
        
        total += count / 2
        
        return total >= n


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 