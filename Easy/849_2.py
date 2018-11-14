# ------------------------------
# 849. Maximize Distance to Closest Person
# 
# Description:
# 
# Version: 2.0
# 10/29/18 by Jianfa
# ------------------------------

class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        people = (i for i, seat in enumerate(seats) if seat)
        
        prev, future = None, next(people)
        
        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            
            else:
                while future is not None and future < i:
                    future = next(people, None)
                
                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))
                
        return ans

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Two pointer solution from solution section.
# Keep track of prev, the filled seat at or to the left of i, and future, the filled seat at or to the right of i. 
# Then at seat i, the closest person is min(i - prev, future - i), with one exception. i - prev should be considered infinite 
# if there is no person to the left of seat i, and similarly future - i is infinite if there is no one to the right of seat i.