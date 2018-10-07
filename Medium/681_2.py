# ------------------------------
# 681. Next Closest Time
# 
# Description:
# 
# Version: 2.0
# 10/06/18 by Jianfa
# ------------------------------

class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hour = int(time[:2])
        minute = int(time[3:])
        res = curr = hour * 60 + minute
        diff = 24 * 60  # Denote the smallest difference of current time and possible time (unit: minute)
        
        digits = (int(time[0]), int(time[1]), int(time[3]), int(time[4]))
        
        for h1, h2, m1, m2 in itertools.product(digits, repeat=4):
            hh = 10 * h1 + h2
            mm = 10 * m1 + m2
            if hh < 24 and mm < 60:  # Eliminate the invalid time
                candidate = hh * 60 + mm
                temp = (candidate - curr) % (24 * 60)
                if 0 < temp < diff:  # Edge case is candidate is current time. Replace res if candidate is closer to current time
                    diff = temp
                    res = candidate
        
        return "{:02d}:{:02d}".format(*divmod(res, 60))

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow the second solution from Solution section
# O(1) time complexity. The worst case is traverse 4*4*4*4 = 256 times
# Check every possible digit combination.