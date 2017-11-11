# ------------------------------
# 568. Maximum Vacation Days
# 
# Description:
# https://leetcode.com/problems/maximum-vacation-days/description/
# 
# Version: 1.0
# 11/10/17 by Jianfa
# ------------------------------

class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        if not flights or not days:
            return 0
        
        dp = [0] * len(days)
        for week in range(len(days[0]))[::-1]:
            temp = [0] * len(days)
            for curr_city in range(len(days)):
                temp[curr_city] = days[curr_city][week] + dp[curr_city]  # Use temp to store result so that don't affect the dp
                for move_to_city in range(len(days)):
                    if flights[curr_city][move_to_city] == 1:
                        temp[curr_city] = max(days[move_to_city][week] + dp[move_to_city], temp[curr_city])
                        
            dp = temp
        
        return dp[0]
        

# ------------------------------
# Summary:
# Dynamic Programming
# https://leetcode.com/problems/maximum-vacation-days/solution/
# Approach 4