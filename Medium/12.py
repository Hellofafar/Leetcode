# ------------------------------
# 12. Integer to Roman
# 
# Description:
# Given an integer, convert it to a roman numeral.
# Input is guaranteed to be within the range from 1 to 3999.
# 
# Version: 1.0
# 09/30/17 by Jianfa
# ------------------------------

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        character = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}

        string = ""

        for i in range(3, -1, -1):
            denominator = pow(10, i)
            digit = num // denominator
            num = num % denominator

            if digit > 0 and digit < 4:
                for _ in range(digit):
                    string += character[denominator]
        
            elif digit == 4:
                string += character[denominator] + character[denominator * 5]
        
            elif digit > 4 and digit < 9:
                string += character[denominator * 5]
                for _ in range(digit - 5):
                    string += character[denominator]
        
            elif digit == 9:
                string += character[denominator] + character[denominator * 10]

            else:
                pass

        return string
            
        
# Used for test
if __name__ == "__main__":
    test = Solution()
    num = 621
    
    print(test.intToRoman(num)) 