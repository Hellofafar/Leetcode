# ------------------------------
# 401. Binary Watch
# 
# Description:
# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
# Each LED represents a zero or one, with the least significant bit on the right.
# 
# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
# Example:
# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
# 
# Note:
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
# 
# Version: 1.0
# 06/28/18 by Jianfa
# ------------------------------

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    if m < 10:
                        res.append(str(h) + ':0' + str(m))
                    else:
                        res.append(str(h) + ':' + str(m))
                        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Brute force search.
# 
# A very brief solution from: https://leetcode.com/problems/binary-watch/discuss/88458/Simple-Python+Java
# def readBinaryWatch(self, num):
#     return ['%d:%02d' % (h, m)
#             for h in range(12) for m in range(60)
#             if (bin(h) + bin(m)).count('1') == num]