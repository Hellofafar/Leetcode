# ------------------------------
# 13. Roman to Integer
# 
# Description:
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.
# 
# Version: 1.0
# 09/15/17 by Jianfa
# ------------------------------

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        character = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        size = len(s)
        if size == 1:
            return character[s]
        else:
            sum = 0
            i = 0
            while i < size - 1:
                c1 = s[i]
                c2 = s[i+1]
                if character[c1] >= character[c2]:
                    sum += character[c1]
                    i += 1
                else:
                    sum += character[c2] - character[c1]
                    i += 2
            if i == size - 1: # If the last character haven't contributed to sum, then add it.
                last_c = s[i]
                sum += character[last_c]
            else:
                pass

            return sum

# Used for test
# if __name__ == "__main__":
#     test = Solution()
#     string = "DCXXI"
    
#     print(test.romanToInt(string)) 