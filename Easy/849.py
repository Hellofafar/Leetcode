# ------------------------------
# 849. Maximize Distance to Closest Person
# 
# Description:
# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 
# There is at least one empty seat, and at least one person sitting.
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
# Return that maximum distance to closest person.
# 
# Example 1:
# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# 
# Example 2:
# Input: [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# 
# Note:
# 1 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.
# 
# Version: 1.0
# 10/29/18 by Jianfa
# ------------------------------

class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        N = len(seats)
        left = [N] * N
        right = [N] * N
        
        for i in range(N):
            if seats[i] == 1:  # It means this seat cannot be sit so left distance is 0
                left[i] = 0
            
            elif i > 0:        # If this seat is empty and it's not the first seat
                left[i] = left[i-1] + 1
        
        for i in range(N-1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            
            elif i < N - 1:
                right[i] = right[i+1] + 1
            
        return max(min(left[i], right[i]) for i, seat in enumerate(seats) if not seat)
                

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# From the first solution.
# Key idea is to use two list left and right, to record the distance of closest person left/right from seat i.
# Note: only when the closest person exists, the distance make sense.