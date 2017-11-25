# ------------------------------
# 406. Queue Reconstruction by Height
# 
# Description:
# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
# 
# Note:
# The number of people is less than 1,100.
# 
# Example
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# 
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
# 
# Version: 1.0
# 11/25/17 by Jianfa
# ------------------------------

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda person: (-person[0], person[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# I didn't come up with this idea myself. Reference is in the discuss section. "Explanation of the neat Sort+Insert solution"