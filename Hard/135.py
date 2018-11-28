# ------------------------------
# 135. Candy
# 
# Description:
# There are N children standing in a line. Each child is assigned a rating value.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
# 
# Example 1:
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# 
# Example 2:
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.
# 
# Version: 1.0
# 10/09/18 by Jianfa
# ------------------------------

class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        
        res = 0
        
        left2right = [1 for _ in range(len(ratings))]  # store the number of candies required by the current student taking care of his left neighbour
        right2left = [1 for _ in range(len(ratings))]  # store the number of candies required by the current student taking care of his right neighbour
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left2right[i] = left2right[i-1] + 1
                
        for i in range(len(ratings) - 1)[::-1]:
            if ratings[i] > ratings[i+1]:
                right2left[i] = right2left[i+1] + 1
                
        for i in range(len(ratings)):
            res += max(left2right[i], right2left[i])
        
        return res
                

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow idea from Solution section
# Use left2right and right2left array to store the number of candy when taking care of 
# neighbour at one side
# Get the max value for each index of left2right and right2left as final result, then sum them