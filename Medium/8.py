# ------------------------------
# 8. String to Integer (atoi)
# 
# Description:
# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary until the first non-whitespace character 
# is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many 
# numerical digits as possible, and interprets them as a numerical value.
# 
# The string can contain additional characters after those that form the integral number, which are ignored and 
# have no effect on the behavior of this function.
# 
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence 
# exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# 
# If no valid conversion could be performed, a zero value is returned.
# 
# Note:
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# 
# Version: 1.0
# 9/21/19 by Jianfa
# ------------------------------

class Solution:
    def myAtoi(self, str: str) -> int:        
        str = str.strip()
        if len(str) == 0:
            return 0
        
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        
        if str[0].isdigit():
            i = 1
            while i < len(str) and str[i].isdigit():
                i += 1
            
            if int(str[0:i]) > INT_MAX:
                return INT_MAX
            else:
                return int(str[0:i])
            
        elif str[0] == '+' or str[0] == '-':
            i = 1
            while i < len(str) and str[i].isdigit():
                i += 1
            
            if i == 1:
                # No numeric character after '+' and '-'
                return 0
            
            elif int(str[0:i]) > INT_MAX:
                return INT_MAX
            
            elif int(str[0:i]) < INT_MIN:
                return INT_MIN
            
            else:
                return int(str[0:i])
            
        else:
            return 0

# Used for testing
if __name__ == "__main__":
    test = Solution()
    str1 = "+"
    str2 = " "

# ------------------------------
# Summary:
# Cover all the situation is the key point. Only two types of strings are possible:
# 1. Start by numeric character
# 2. Start by + or -