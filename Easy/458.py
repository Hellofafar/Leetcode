# ------------------------------
# 458. Poor Pigs
# 
# Description:
# There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. They all look the same. If a pig drinks that poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.
# Answer this question, and write an algorithm for the follow-up general case.
# 
# Follow-up:
# If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the "poison" bucket within p minutes? There is exact one bucket with poison.
# 
# Version: 1.0
# 07/07/18 by Jianfa
# ------------------------------

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
            
        return pigs

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# A math problem. Here is a good explanation: https://leetcode.com/problems/poor-pigs/discuss/94266/Another-explanation-and-solution