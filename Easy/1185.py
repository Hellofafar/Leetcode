# ------------------------------
# 1185. Day of the Week
# 
# Description:
# Given a date, return the corresponding day of the week for that date.
# 
# The input is given as three integers representing the day, month and year respectively.
# 
# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", 
# "Thursday", "Friday", "Saturday"}.
# 
# Example 1:
# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"
# 
# Example 2:
# Input: day = 18, month = 7, year = 1999
# Output: "Sunday"
# 
# Example 3:
# Input: day = 15, month = 8, year = 1993
# Output: "Sunday"
# 
# Constraints:
# The given dates are valid dates between the years 1971 and 2100.
# 
# Version: 1.0
# 11/07/19 by Jianfa
# ------------------------------

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        y = 1971
        count = 0
        # first count dates of previous years before year
        while y != year:
            if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
                count += 366
            else:
                count += 365
            y += 1
        
        m = 1
        leapYear = year % 400 == 0 or year % 4 == 0 and year % 100 != 0
        # then count dates of previous months before month
        while m != month:
            if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10:
                count += 31
            elif m == 4 or m == 6 or m == 9 or m == 11:
                count += 30
            elif m == 2:
                if leapYear:
                    count += 29
                else:
                    count += 28
            m += 1
        
        count += day - 1 # minus 1/1/1971
        
        # 01/01/1971 is Friday
        dayDict = {0:"Friday", 1:"Saturday", 2:"Sunday", 3:"Monday", 4:"Tuesday", 5:"Wednesday", 6:"Thursday"}
        return dayDict[count%7]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Just have to know 01/01/1971 is Friday.